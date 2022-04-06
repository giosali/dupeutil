<h1 align="center">dupeutil</h1>

<p align="center">
    <a href="https://pypi.org/project/dupeutil">
        <img src="https://img.shields.io/pypi/v/dupeutil" alt="PyPI Version">
    </a>
    <a href="https://pypi.org/project/dupeutil">
        <img src="https://img.shields.io/pypi/pyversions/dupeutil" alt="Supported Python Versions">
    </a>
</p>

<p align="center">
    <a href="https://github.com/psf/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style">
    </a>
    <a href="https://github.com/giosali/dupeutil/actions/workflows/tests.yml">
		<img src="https://github.com/giosali/dupeutil/actions/workflows/tests.yml/badge.svg" alt="Tests">
	</a>
    <a href="https://codecov.io/gh/giosali/dupeutil">
        <img src="https://codecov.io/gh/giosali/dupeutil/branch/main/graph/badge.svg?token=AAXB6Q0SJA" alt="Code Coverage">
    </a>
    <a href="https://github.com/giosali/dupeutil/blob/main/LICENSE">
        <img src="https://img.shields.io/pypi/l/dupeutil" alt="License">
    </a>
</p>

<p align="center">
    A command-line program written in Python for detecting and removing duplicate files
</p>

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
  * [Arguments](#arguments)
    + [Files flag](#files-flag)
    + [Quiet flag](#quiet-flag)
    + [Recursive flag](#recursive-flag)

## Installation

To install **dupeutil**, enter the following command in your terminal:

```
python -m pip install dupeutil
```

## Usage

**dupeutil** is designed to be as effortless and as easy as possible to use. You can check for duplicate files in a directory by `cd`-ing into that directory and by simply entering the following command in your terminal:

```
dupeutil
```

That's it. The program will then check for duplicate files in the *current working directory* and provide you with a prompt that shows which duplicates were found and ask if you would like to remove them.

<img src="https://raw.githubusercontent.com/giosali/dupeutil/main/ext/example.png" alt="Example" width="450">

Alternatively, if you would like to check a particular directory without it being the current working directory, you can explicitly pass it a directory:

```
dupeutil <path to dir>
```

```
📝 NOTE: You may need to wrap the directory in quotes:

dupeutil "C:\Users\user\Downloads\folder"
```

### Arguments

These are the available command-line arguments that you can pass to **dupeutil**. You can enter `dupeutil -h` or `dupeutil --help` in your terminal to view them as well.

```
positional arguments:
  dir                           the directory to check

options:
  -h, --help                    show this help message and exit
  -f FILES [FILES ...],         the files to compare
  --files FILES [FILES ...]

  -q, --quiet                   suppress output to the console; this option will not ask for
                                permission to  remove files
  -r, --recursive               include files in subdirectories
  -v, --version                 print program version
```

#### Files flag

If you'd rather compare files instead of a directory, you can do so by using the `-f` or `--files` flag:

```
dupeutil -f <path to file1> <path to file2> <path to file3> ... <path to fileN>
```

If any of the paths contain a space, it's recommended that you wrap them in quotes.

#### Quiet flag

If you don't want to see any output in the console, you can pass the `-q` or `--quiet` flag when you run **dupeutil**:

```
dupeutil <path to dir> -q
```

If you include the quiet flag, the program will not provide you with an overview of duplicate files, nor will it ask you for permission to remove those files.

#### Recursive flag

If you would like to include subdirectories in the given directory, pass the `-r` or `--recursive` flag:

```
dupeutil <path to dir> -r
```

Including this flag will cause files in the top-level directory and files in any subdirectories to be compared as well.