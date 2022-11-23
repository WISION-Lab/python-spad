#!/usr/bin/env python3

from argparse import ArgumentParser
from math import prod
from pathlib import Path

import numpy as np
from numpy.lib.format import open_memmap


def main(args):
    input_path = Path(args.input_pathname)
    bin_paths = list(input_path.glob("**/*.bin"))
    bin_paths.sort(key=lambda f: int(f.stem.replace("filename", "")))

    n_frames = 0
    for bin_path in bin_paths:
        n_frames += bin_path.stat().st_size * 8 // prod(args.size)

    data = open_memmap(
        args.output_pathname,
        mode="w+",
        dtype="uint8",
        shape=(n_frames, args.size[0], (args.size[1] + 7) // 8),
    )
    offset = 0
    for bin_path in bin_paths:
        x = np.fromfile(bin_path, dtype="uint8")
        x = np.unpackbits(x, bitorder="little")
        x = np.reshape(x, (-1,) + tuple(args.size))
        x = np.packbits(x, axis=-1)
        data[offset : offset + x.shape[0]] = x
        offset += x.shape[0]
    print(f"Saved {args.output_pathname}")


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "input_pathname",
        help="an input directory containing one or more .bin files (possibly nested)",
    )
    parser.add_argument(
        "output_pathname", help="an output filename with extension .npz"
    )
    parser.add_argument(
        "-s",
        "--size",
        default=[256, 512],
        nargs=2,
        type=int,
        help="the size to assume for the image",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
