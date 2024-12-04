import os
from datetime import datetime
import time
from enum import Enum

import requests
from dotenv import load_dotenv

load_dotenv()

_AOC_COOKIE = os.getenv('AOC_COOKIE')
_CUR_YEAR = datetime.now().year


class SOURCE(Enum):
    EXAMPLE = 1
    INPUT = 2


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


def get_data(src: SOURCE, day: int, year=_CUR_YEAR, offset=0) -> str:
    data = ''
    if src == SOURCE.EXAMPLE:
        data = _get_example(day, year=year, offset=offset)
    elif src == SOURCE.INPUT:
        data = _get_input(day, year=year)
    return data.strip()


def benchmark(title, function):
    start_time = time.time()
    result = function()
    print(f"{title}{' ' * (10 - len(title))} \t Time: {round(time.time() - start_time, 10)} \t Result: {result}")
