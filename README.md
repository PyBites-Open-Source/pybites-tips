# PyBites Tips CLI

A wrapper to read [PyBites Python tips](https://codechalleng.es/tips) from the command line.

## Installation

You can install the PyBites Tips CLI from [PyPI](https://pypi.org/project/pybites-tips/):

    pip install pybites-tips

This tool uses Python 3.x

## Usage

PyBites Tips CLI is a command line application. There are two modes to run it:

1. Interactive mode:

		$ pytip

		Search tips (press 'q' to exit): functools
		3 tips found

		=== TIP 153 ===
		Title: functools.partial
		...
		...

2. Search for tips from the command line using the `-s` flag:

		$ pytip -s itertools
		7 tips found

		=== TIP 53 ===
		Title: random.choice and itertools.product
		Tip: #Python's random, range and itertools.product make it easy to simulate 5 dice rolls:
		...
		...

If you want to _page_ through the results use the `-p` flag:

	$ pytip -s itertools
	7 tips found

	Press any key to start paging them, then press 'q' to go to the next one ... or hit 'c' bail out:
	...
	<< results page paged (you see them one by one in terminal) >>

Alternatively just pip `pytip`'s output to `more`: `pytip -s itertools|more`
