#!/usr/bin/env python3

from argparse import ArgumentParser

import numpy as np
from scipy.io import loadmat


def main(args):
    x = loadmat(args.input_pathname)
    np.savez(args.output_pathname, **x)
    print(f"Saved {args.output_pathname}")


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("input_pathname", help="an input filename with extension .mat")
    parser.add_argument(
        "output_pathname", help="an output filename with extension .npz"
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
