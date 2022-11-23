#!/usr/bin/env python3

import json
from argparse import ArgumentParser
from pathlib import Path

import numpy as np
from numpy.lib.format import open_memmap
from scipy.io import loadmat


def main(args):
    with open(Path(args.input_pathname, "info.json"), "r") as info_file:
        n_parts = json.load(info_file)["no_parts"]

    data = None
    for i in range(n_parts):
        part_path = Path(args.input_pathname, f"part_{i + 1}.mat")
        x = loadmat(str(part_path))["OUTPUT"]
        x = np.transpose(x, (2, 0, 1))
        x = np.packbits(x, axis=-1)
        if data is None:
            data = open_memmap(
                args.output_pathname,
                mode="w+",
                dtype="uint8",
                shape=(n_parts * x.shape[0],) + x.shape[1:],
            )
        data[i * x.shape[0] : (i + 1) * x.shape[0]] = x
    print(f"Saved {args.output_pathname}")


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "input_pathname",
        help="an input directory containing a .json file and one or more .mat files",
    )
    parser.add_argument(
        "output_pathname", help="an output filename with extension .npz"
    )
    parser.add_argument("-q", "--quiet", help="don't print status updates")
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
