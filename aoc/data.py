import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from aoc import SOURCE

load_dotenv()

_AOC_COOKIE = os.getenv('AOC_COOKIE')
_CUR_YEAR = datetime.now().year


def _get_input(day: int, year: int) -> str:
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",
                            cookies={'session': _AOC_COOKIE})
    if response.status_code != 200:
        return ''
    return response.text


def _get_example(day: int, year: int, offset: int) -> str:
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}",
                            cookies={'session': _AOC_COOKIE})
    if response.status_code != 200:
        return ''
    blocks = response.text.split('<pre><code>')
    return blocks[offset + 1].split('</code></pre>')[0]


def get_data(src: SOURCE, day: int, year=_CUR_YEAR, offset=0) -> str:
    data = ''
    if src == SOURCE.EXAMPLE:
        data = _get_example(day, year=year, offset=offset)
    elif src == SOURCE.INPUT:
        data = _get_input(day, year=year)
    return data.strip()
