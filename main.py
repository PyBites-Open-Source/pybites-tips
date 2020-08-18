import argparse

import requests

API = "https://codechalleng.es/api/tips/{search_string}"


def get_tips(search=None):
    pass


def show_tips(tips):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search term')
    parser.add_argument("-s", "--search", type=str, required=True,
                        help='Search PyBites Python tips')
    args = parser.parse_args()
    tips = get_tips(args.search)
    show_tips(tips)
