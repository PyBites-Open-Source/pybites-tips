import argparse
from collections import namedtuple
import pydoc

import requests

TIPS_API_ENDPOINT = "https://codechalleng.es/api/tips/"

Tip = namedtuple('Tip', ('id title tip code '
                         'link image_link share_link'))
EXIT, CANCEL = 'q', 'c'
TIP = """
=== TIP {id} ===
Title: {title}
Tip: {tip}

Code:
{code}

Links:
{links}
---
"""


class PyBitesTips:

    def __init__(self):
        self.tips = self._get_tips()

    def _get_tips(self):
        resp = requests.get(TIPS_API_ENDPOINT)
        resp.raise_for_status()
        return [Tip(**tip) for tip in resp.json()]

    def filter_tips(self, search):
        search = search.lower()
        return sorted(
            [tip for tip in self.tips if search in
             (tip.title + tip.tip + tip.code).lower()],
            key=lambda tip: tip.id)

    def show_tips(self, tips):
        hits = len(tips)
        if hits == 0:
            print("No hits, try another search term")
            return
        elif hits > 1:
            # if multiple tips, explain paging interface
            print(f"{hits} tips found")
            choice = input(
                ("\nPress any key to start paging them, "
                 f"then press '{EXIT}' to go to the next one ... "
                 f"or hit '{CANCEL}' bail out: ")
            )
            if choice == CANCEL:
                return
        self.print_tips(tips)

    def _generate_tip_output(self, tip):
        links = '\n'.join(
            link for link in
            (tip.link, tip.image_link, tip.share_link)
            if link)
        return TIP.format(id=tip.id,
                          title=tip.title,
                          tip=tip.tip,
                          code=tip.code,
                          links=links)

    def print_tips(self, tips):
        for tip in tips:
            tip_fmt = self._generate_tip_output(tip)
            pydoc.pager(tip_fmt)

    def __call__(self):
        while True:
            search = input(
                f"\nSearch tips (press '{EXIT}' to exit): ")
            if not search.strip():
                print("Please enter a search term")
                continue
            if search == EXIT:
                print("Bye")
                break
            tips = self.filter_tips(search)
            self.show_tips(tips)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search term')
    parser.add_argument("-s", "--search", type=str,
                        help='Search PyBites Python tips')

    args = parser.parse_args()

    pb_tips = PyBitesTips()
    if args.search:
        tips = pb_tips.filter_tips(args.search)
        pb_tips.show_tips(tips)
    else:
        pb_tips()
