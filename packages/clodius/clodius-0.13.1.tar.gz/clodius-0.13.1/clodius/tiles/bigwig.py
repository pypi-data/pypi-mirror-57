import bbi
import clodius.tiles.format as hgfo
import functools as ft
import logging
import numpy as np
import pandas as pd
import re

from concurrent.futures import ThreadPoolExecutor

MAX_THREADS = 4
TILE_SIZE = 1024

logger = logging.getLogger(__name__)

aggregation_modes = {}
aggregation_modes["mean"] = {"name": "Mean", "value": "mean"}
aggregation_modes["min"] = {"name": "Min", "value": "min"}
aggregation_modes["max"] = {"name": "Max", "value": "max"}
aggregation_modes["std"] = {"name": "Standard Deviation", "value": "std"}

range_modes = {}
range_modes["minMax"] = {"name": "Min-Max", "value": "minMax"}
range_modes["whisker"] = {"name": "Whisker", "value": "whisker"}


def get_quadtree_depth(chromsizes):
    tile_size_bp = TILE_SIZE
    min_tile_cover = np.ceil(sum(chromsizes) / tile_size_bp)
    return int(np.ceil(np.log2(min_tile_cover)))


def get_zoom_resolutions(chromsizes):
    return [2 ** x for x in range(get_quadtree_depth(chromsizes) + 1)][::-1]


def natsort_key(s, _NS_REGEX=re.compile(r"(\d+)", re.U)):
    return tuple([int(x) if x.isdigit() else x for x in _NS_REGEX.split(s) if x])


def natcmp(x, y):
    if x.find("_") >= 0:
        x_parts = x.split("_")
        if y.find("_") >= 0:
            # chr_1 vs chr_2
            y_parts = y.split("_")

            return natcmp(x_parts[1], y_parts[1])
        else:
            # chr_1 vs chr1
            # chr1 comes first
            return 1
    if y.find("_") >= 0:
        # chr1 vs chr_1
        # y comes second
        return -1

    _NS_REGEX = re.compile(r"(\d+)", re.U)
    x_parts = tuple([int(a) if a.isdigit() else a for a in _NS_REGEX.split(x) if a])
    y_parts = tuple([int(a) if a.isdigit() else a for a in _NS_REGEX.split(y) if a])

    # order of these parameters is purposefully reverse how they should be
    # ordered
    for key in ["m", "y", "x"]:
        if key in y.lower():
            return -1
        if key in x.lower():
            return 1

    try:
        if x_parts < y_parts:
            return -1
        elif y_parts > x_parts:
            return 1
        else:
            return 0
    except TypeError:
        return 1


def natsorted(iterable):
    return sorted(iterable, key=ft.cmp_to_key(natcmp))


def get_chromsizes(bwpath):
    """
    TODO: replace this with negspy

    Also, return NaNs from any missing chromosomes in bbi.fetch

    """
    chromsizes = bbi.chromsizes(bwpath)
    chromosomes = natsorted(chromsizes.keys())
    chrom_series = pd.Series(chromsizes)[chromosomes]
    return chrom_series


def abs2genomic(chromsizes, start_pos, end_pos):
    abs_chrom_offsets = np.r_[0, np.cumsum(chromsizes.values)]
    cid_lo, cid_hi = (
        np.searchsorted(abs_chrom_offsets, [start_pos, end_pos], side="right") - 1
    )
    rel_pos_lo = start_pos - abs_chrom_offsets[cid_lo]
    rel_pos_hi = end_pos - abs_chrom_offsets[cid_hi]
    start = rel_pos_lo
    for cid in range(cid_lo, cid_hi):
        yield cid, start, chromsizes[cid]
        start = 0
    yield cid_hi, start, rel_pos_hi


def tileset_info(bwpath, chromsizes=None):
    """
    Get the tileset info for a bigWig file

    Parameters
    ----------
    bwpath: string
        The path to the bigwig file from which to retrieve data
    chromsizes: [[chrom, size],...]
        A list of chromosome sizes associated with this tileset.
        Typically passed in to specify in what order data from
        the bigwig should be returned.

    Returns
    -------
    tileset_info: {'min_pos': [],
                    'max_pos': [],
                    'tile_size': 1024,
                    'max_zoom': 7
                    }
    """
    TILE_SIZE = 1024

    if chromsizes is None:
        chromsizes = get_chromsizes(bwpath)
        chromsizes_list = []

        for chrom, size in chromsizes.iteritems():
            chromsizes_list += [[chrom, int(size)]]
    else:
        chromsizes_list = chromsizes

    min_tile_cover = np.ceil(sum([int(c[1]) for c in chromsizes_list]) / TILE_SIZE)
    max_zoom = int(np.ceil(np.log2(min_tile_cover)))

    tileset_info = {
        "min_pos": [0],
        "max_pos": [TILE_SIZE * 2 ** max_zoom],
        "max_width": TILE_SIZE * 2 ** max_zoom,
        "tile_size": TILE_SIZE,
        "max_zoom": max_zoom,
        "chromsizes": chromsizes_list,
        "aggregation_modes": aggregation_modes,
        "range_modes": range_modes,
    }
    return tileset_info


def fetch_data(a):
    (bwpath, binsize, chromsizes, aggregation_mode, range_mode, cid, start, end) = a
    n_bins = int(np.ceil((end - start) / binsize))
    n_dim = 1

    if range_mode == "minMax":
        n_dim = 2

    if range_mode == "whisker":
        n_dim = 4

    x = np.zeros((n_bins, n_dim)) if n_dim > 1 else np.zeros(n_bins)

    try:
        chrom = chromsizes.index[cid]
        clen = chromsizes.values[cid]

        args = [bwpath, chrom, start, end]
        kwargs = {"bins": n_bins, "missing": np.nan}

        if range_mode == "minMax":
            x[:, 0] = bbi.fetch(*args, **dict(kwargs, summary="min"))
            x[:, 1] = bbi.fetch(*args, **dict(kwargs, summary="max"))

        elif range_mode == "whisker":
            x[:, 0] = bbi.fetch(*args, **dict(kwargs, summary="min"))
            x[:, 1] = bbi.fetch(*args, **dict(kwargs, summary="max"))
            x[:, 2] = bbi.fetch(*args, **dict(kwargs, summary="mean"))
            x[:, 3] = bbi.fetch(*args, **dict(kwargs, summary="std"))

        else:
            x[:] = bbi.fetch(*args, **dict(kwargs, summary=aggregation_mode))

        # drop the very last bin if it is smaller than the binsize
        if end == clen and clen % binsize != 0:
            x = x[:-1]
    except IndexError:
        # beyond the range of the available chromosomes
        # probably means we've requested a range of absolute
        # coordinates that stretch beyond the end of the genome
        x[:] = np.nan
    except KeyError:
        # probably requested a chromosome that doesn't exist (e.g. chrM)
        x[:] = np.nan

    return x


def get_bigwig_tile(
    bwpath,
    zoom_level,
    start_pos,
    end_pos,
    chromsizes=None,
    aggregation_mode="mean",
    range_mode=None,
):
    if chromsizes is None:
        chromsizes = get_chromsizes(bwpath)

    resolutions = get_zoom_resolutions(chromsizes)
    binsize = resolutions[zoom_level]

    cids_starts_ends = list(abs2genomic(chromsizes, start_pos, end_pos))
    with ThreadPoolExecutor(max_workers=16) as e:
        arrays = list(
            e.map(
                fetch_data,
                [
                    tuple(
                        [bwpath, binsize, chromsizes, aggregation_mode, range_mode]
                        + list(c)
                    )
                    for c in cids_starts_ends
                ],
            )
        )

    return np.concatenate(arrays)


def tiles(bwpath, tile_ids, chromsizes_map={}, chromsizes=None):
    """
    Generate tiles from a bigwig file.

    Parameters
    ----------
    tileset: tilesets.models.Tileset object
        The tileset that the tile ids should be retrieved from
    tile_ids: [str,...]
        A list of tile_ids (e.g. xyx.0.0) identifying the tiles
        to be retrieved
    chromsizes_map: {uid: []}
        A set of chromsizes listings corresponding to the parameters of the
        tile_ids. To be used if a chromsizes id is passed in with the tile id
        with the `|cos:id` tag in the tile id
    chromsizes: [[chrom, size],...]
        A 2d array containing chromosome names and sizes. Overrides the
        chromsizes in chromsizes_map

    Returns
    -------
    tile_list: [(tile_id, tile_data),...]
        A list of tile_id, tile_data tuples
    """
    TILE_SIZE = 1024
    generated_tiles = []
    for tile_id in tile_ids:
        tile_option_parts = tile_id.split("|")[1:]
        tile_no_options = tile_id.split("|")[0]
        tile_id_parts = tile_no_options.split(".")
        tile_position = list(map(int, tile_id_parts[1:3]))
        return_value = tile_id_parts[3] if len(tile_id_parts) > 3 else "mean"

        aggregation_mode = return_value if return_value in aggregation_modes else "mean"
        range_mode = return_value if return_value in range_modes else None

        tile_options = dict([o.split(":") for o in tile_option_parts])

        if chromsizes:
            chromnames = [c[0] for c in chromsizes]
            chromlengths = [int(c[1]) for c in chromsizes]
            chromsizes_to_use = pd.Series(chromlengths, index=chromnames)
        else:
            chromsizes_id = None
            if "cos" in tile_options:
                chromsizes_id = tile_options["cos"]
            if chromsizes_id in chromsizes_map:
                chromsizes_to_use = chromsizes_map[chromsizes_id]
            else:
                chromsizes_to_use = None

        zoom_level = tile_position[0]
        tile_pos = tile_position[1]

        # this doesn't combine multiple consequetive ids, which
        # would speed things up
        if chromsizes_to_use is None:
            chromsizes_to_use = get_chromsizes(bwpath)

        max_depth = get_quadtree_depth(chromsizes_to_use)
        tile_size = TILE_SIZE * 2 ** (max_depth - zoom_level)
        start_pos = tile_pos * tile_size
        end_pos = start_pos + tile_size
        dense = get_bigwig_tile(
            bwpath,
            zoom_level,
            start_pos,
            end_pos,
            chromsizes_to_use,
            aggregation_mode=aggregation_mode,
            range_mode=range_mode,
        )

        tile_value = hgfo.format_dense_tile(dense)

        generated_tiles += [(tile_id, tile_value)]
    return generated_tiles


def chromsizes(filename):
    """
    Get a list of chromosome sizes from this [presumably] bigwig
    file.

    Parameters:
    -----------
    filename: string
        The filename of the bigwig file

    Returns
    -------
    chromsizes: [(name:string, size:int), ...]
        An ordered list of chromosome names and sizes
    """
    try:
        chrom_series = get_chromsizes(filename)
        data = []
        for chrom, size in chrom_series.iteritems():
            data.append([chrom, size])
        return data
    except Exception as ex:
        logger.error(ex)
        raise Exception("Error loading chromsizes from bigwig file: {}".format(ex))
