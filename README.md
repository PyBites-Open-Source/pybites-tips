# PyBites Tips CLI

A wrapper to read [PyBites Python tips](https://codechalleng.es/tips) from the command line.

## Installation

You can install the PyBites Tips CLI from [PyPI](https://pypi.org/project/pybites-tips/):

    pip install pybites-tips

This tool uses Python 3.x

## Usage

PyBites Tips CLI is a command line application. There are two modes to run it:

1. Interactive mode:

	>>> from src import PyBitesTips
	>>> pb = PyBitesTips()
	>>> pb()

	Search tips (press 'q' to exit): wraps
	2 tips found

	Press any key to start paging them, then press 'q' to go to the next one ... or hit 'c' bail out:

	>> tips are paged to the console <<

	Search tips (press 'q' to exit): q
	Bye

2. Search for tips with the `-s` flag:

	$ pytip -s itertools
	7 tips found

	Press any key to start paging them, then press 'q' to go to the next one ... or hit 'c' bail out:
	...
