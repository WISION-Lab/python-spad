# Working With SPAD Data

## Organization

The `dark` directory countains dark count data. The data in this folder has all been converted to `.npy` or `.npy`, but the array shapes and data types vary (information about this data's format was not documented in the original dataset).

The `sequences` directory contains one sub-directory for each sequence. For example, `sequences/0505-bicycle-1` contains all data for the `0505-bicycle-1` sequence. In each sequence directory there is a `binary.npy.gz` file containing all SPAD frames. A sequence directory may also contain other related files - for example, an `.mp4` video captured by a conventional camera.

The `misc` directory contains miscellaneous video files.

The `results` directory is an exact copy of the `results` directory from the original dataset.

## Format

Uncomopress `binary.npy.gz` to `binary.npy` file using the command
```
gunzip binary.npy.gz
```
Use `unpigz` instead of `gunzip` for faster, multi-threaded processing.

Read `.npy` files using the following Python code:
```python
import numpy as np
data = np.load("binary.npy")
data = np.unpackbits(data, axis=-1)
```
Before unpacking, `data` is a bit-packed array of shape `(t, h, w / 8)` and type `uint8`. After unpacking, `data` is a binary array of shape `(t, h, w)` and type `uint8`.

## Memory Concerns

The above code allocates an entire byte of memory for each binary element of the `(t, h, w)` array. For long sequences, this can easily exhaust the available system memory.

There are a couple of techniques we can use here. The first is to unpack the bits of each frame on the fly. So, instead of this:
```python
# Load data
data = np.unpackbits(data, axis=-1)
for frame in data:
    # Do something with frame
```
do this:
```python
# Load data
for frame in data:
    frame = np.unpackbits(frame, axis=-1)
    # Do something with frame
```
For extremely large arrays (where even the packed array doesn't fit into memory) we can use memory mapping. This means replacing this code:
```python
data = np.load("binary.npy")
```
with this code:
```python
data = np.load("binary.npy", mmap_mode="r")
```
With memory mapping, pieces of the array will only be loaded into memory when accessed. See the NumPy documentation for more details.
