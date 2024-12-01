import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

AOC_COOKIE = os.getenv("AOC_COOKIE")

SRC_EXAMPLE = 'example'
SRC_FILE = 'input'
CUR_YEAR = datetime.now().year


def get_input(day, year=CUR_YEAR):
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",
                            headers={"cookie": "session=" + AOC_COOKIE})
    return response.text


def get_example(day, year=CUR_YEAR, offset=0):
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}",
                            headers={"cookie": "session=" + AOC_COOKIE})
    blocks = response.text.split("<pre><code>")
    return blocks[offset + 1].split("</code></pre>")[0]


def get_data(src, day, offset=0) -> (list, list):
    data = ""
    if src == SRC_EXAMPLE:
        data = get_example(day, offset=offset)
    elif src == SRC_FILE:
        data = get_input(1)
    return data
