# Day 2: Gift Shop

from functools import partial

import aoc


def get_data(source):
    data = aoc.get_data(src=source, year=2025, day=2)
    data = data.replace('\n','').split(',')
    data = list(map(lambda seq: tuple(seq.split('-')), data))
    return data


def part1(data):
    invalid_ids = []
    for seq in data:
        begin = int(seq[0])
        end = int(seq[1])

        for i in range(begin, end+1):
            cur_id = str(i)
            if not len(cur_id) % 2 and cur_id[:len(cur_id)//2] == cur_id[len(cur_id)//2:]:
                invalid_ids.append(cur_id)

    return sum(map(int, invalid_ids))


def part2(data):
    invalid_ids = []
    for seq in data:
        begin = int(seq[0])
        end = int(seq[1])

        # check each id
        for i in range(begin, end+1):
            cur_id = str(i)
            cur_id_len = len(cur_id)

            # determine which dividers result in even sections for the current id
            even_dividers = [a for a in range(2, cur_id_len+1) if cur_id_len % a == 0]

            # divide the id in even sections
            for j in even_dividers:
                step = cur_id_len // j
                sections = [cur_id[k:k+step] for k in range(0, cur_id_len, step)]

                # the id is found invalid in one of the tested configurations
                if len(set(sections)) == 1:
                    invalid_ids.append(cur_id)
                    break

    return sum(map(int, invalid_ids))


if __name__ == '__main__':
    aoc_data = get_data(aoc.SOURCE.EXAMPLE)
    aoc.benchmark('Part 1', partial(part1, aoc_data))
    aoc.benchmark('Part 2', partial(part2, aoc_data))
