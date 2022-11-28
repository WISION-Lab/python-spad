## Code

`bin_to_npy.py`: A script that converts a collection of `.bin` files to a single `.npy` file. Pass the `--help` flag for information on usage and options.

`loader_example.py`: A script demonstrating usage of the `SPADLoader` class.

`loader.py`: Defines the `SPADLoader` class for iterating over SPAD frames stored in a collection of `.mat` files.

`mat_to_npy.py`: A script that converts a collection of `.mat` files (along with a single `info.json` file) to a single `.npy` file. Pass the `--help` flag for information on usage and options.

`mat_to_npy_raw.py`: A script that converts a single `.mat` file (containing one array) to a `.npy` file, without modifying the shape or data type. Pass the `--help` flag for information on usage and options.

`mat_to_npz_raw.py`: A script that converts a single `.mat` file (containing one or more arrays) to a non-compressed `.npz` file, without modifying the shapes or data types. Pass the `--help` flag for information on usage and options.

## Conda Environment

To create the Conda environment, run:
```
conda env create -f environment.yml
```

## Code Style

Format all code using [Black](https://black.readthedocs.io/en/stable/). Use a line limit of 88 characters (the default). To format a file, use the command:
```
black <FILE>
```
Black is installed in the Conda environment.
