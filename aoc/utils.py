import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

_AOC_COOKIE = os.getenv('AOC_COOKIE')
_CUR_YEAR = datetime.now().year

SRC_EXAMPLE = 'example'
SRC_INPUT = 'input'


def _get_input(day: int, year: int) -> str:
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",
                            headers={'cookie': 'session=' + _AOC_COOKIE})
    if response.status_code != 200:
        return ''
    return response.text


def _get_example(day: int, year: int, offset: int) -> str:
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}",
                            headers={'cookie': 'session=' + _AOC_COOKIE})
    if response.status_code != 200:
        return ''
    blocks = response.text.split('<pre><code>')
    return blocks[offset + 1].split('</code></pre>')[0]


def get_data(src: str, day: int, year=_CUR_YEAR, offset=0) -> str:
    data = ''
    if src == SRC_EXAMPLE:
        data = _get_example(day, year=year, offset=offset)
    elif src == SRC_INPUT:
        data = _get_input(day, year=year)
    return data.strip()
