from unittest.mock import patch, Mock

import pytest
import requests

from src import PyBitesTips

tips_payload = [
    {'code': ">>> 'Python' ' is ' 'fun'\r\n'Python is fun'",
     'id': 11,
     'image_link': None,
     'link': None,
     'share_link': 'https://twitter.com/pybites/status/1106182595866513409',
     'tip': 'String literals will concatenate in #Python:',
     'title': 'concatenate string literals'},
    {'code': '>>> list(range(1, 11))\r\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]',
     'id': 10,
     'image_link': None,
     'link': 'https://codechalleng.es/bites/1',
     'share_link': 'https://twitter.com/pybites/status/1112944740830531585',
     'tip': 'In #Python you can use the range builtin to generate '
            'a sequence of numbers',
     'title': 'range'},
    {'code': ">>> names = 'bob julian tim sara'.split()\r\n"
             ">>> names\r\n"
             "['bob', 'julian', 'tim', 'sara']",
     'id': 8,
     'image_link': None,
     'link': None,
     'share_link': 'https://twitter.com/pybites/status/1111157389317808129',
     'tip': 'An easy way to make a list in #Python is to use split()'
            ' on a string which splits on space by default:',
     'title': 'split a string into a list'}
]


@pytest.fixture
@patch.object(requests, 'get')
def pb_tips(mockget, scope="module"):
    mockget.return_value = Mock(raise_for_status=lambda: None,
                                json=lambda: tips_payload,
                                status_code=200)
    pb_tips = PyBitesTips()
    assert len(pb_tips.tips) == 3
    return pb_tips


def test_tip_output(pb_tips):
    first_tip = pb_tips.tips[0]
    actual = pb_tips._generate_tip_output(first_tip)
    expected = (
        "\n=== TIP 11 ===\n"
        "Title: concatenate string literals\n"
        "Tip: String literals will concatenate in #Python:\n\n"
        "Code:\n>>> 'Python' ' is ' 'fun'\r\n'Python is fun'\n\n"
        "Links:\nhttps://twitter.com/pybites/status/1106182595866513409\n"
        "---\n")
    assert actual == expected


@pytest.mark.parametrize("search, expected", [
    ("julian", [8]),
    ("twitter", []),
    ("string", [8, 11]),
    ("STRING", [8, 11]),
    ("range", [10]),
    ("pYthon", [8, 10, 11]),
    (">>>", [8, 10, 11]),
    ("split", [8]),
    ("literal", [11]),
    ("list", [8, 10]),
])
def test_filter_tips(search, expected, pb_tips):
    tips = pb_tips.filter_tips(search)
    returned_ids = [tip.id for tip in tips]
    assert returned_ids == expected
