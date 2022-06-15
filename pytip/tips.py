from collections import namedtuple
import pydoc
from rich.syntax import Syntax
from rich.console import Console
import os
import requests
from colorama import init

# Windows shells (pycharm) act weird without this when printing colors...
if os.name == 'nt':
    init(autoreset=True)

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

console = Console()

class PyBitesTips:

    def __init__(self, use_pager=False):
        self.use_pager = use_pager
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
            # if multiple tips and pager, explain interface
            print(f"{hits} tips found")
            if self.use_pager:
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

        # Highlight the code with rich syntax highlighter
        code_highlighted = Syntax(tip.code, "python")

        # We don't want to use console.print as output, so we use capture()
        with console.capture() as capture:
            console.print(code_highlighted)
        code_output = capture.get()

        return TIP.format(id=tip.id,
                          title=tip.title,
                          tip=tip.tip,
                          code=code_output,
                          links=links)

    def print_tips(self, tips):
        for tip in tips:
            tip_fmt = self._generate_tip_output(tip)
            if self.use_pager:
                pydoc.pager(tip_fmt)
            else:
                print(tip_fmt)

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
