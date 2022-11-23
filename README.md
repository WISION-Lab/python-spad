## Code

`bin_to_npy.py`: A script that converts a collection of `.bin` files to a single `.npy` file. Pass the `--help` flag for information on usage and options.

`loader_example.py`: A script demonstrating usage of the `SPADLoader` class.

`loader.py`: Defines the `SPADLoader` class for iterating over SPAD frames stored in a collection of `.mat` files.

`mat_to_npy.py`: A script that converts a collection of `.mat` files to a single `.npy` file. Pass the `--help` flag for information on usage and options.

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
