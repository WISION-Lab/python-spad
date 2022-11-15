#!/usr/bin/env python3

from pathlib import Path

from loader import SPADLoader

base_path = Path("/nobackup2", "shared", "quanta_vision")
test_path_1 = base_path.joinpath(
    "siggraph20", "0119-painting2-f11-20khz-1", "binary_images"
)
test_path_2 = base_path.joinpath("vision", "210505", "0505-bicycle-1", "output_images")

for test_path in test_path_1, test_path_2:
    print(f"Path: {test_path}")
    loader = SPADLoader(test_path)
    for i, frame in enumerate(loader):
        print(f"Frame: {i + 1}/{len(loader)} - Shape: {frame.shape}", end="\r")
    print()
