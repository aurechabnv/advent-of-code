SRC_EXAMPLE = 'example'
SRC_FILE = 'file'

def get_lists(source) -> (list, list):
    list1, list2 = [], []

    if source == 'example':
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]

    elif source == 'file':
        with open("day_1_input.txt") as f:
            data = f.readlines()

        for line in data:
            split_line = line.split('  ')
            list1.append(int(split_line[0]))
            list2.append(int(split_line[1]))

    return list1, list2

def get_total_distance(list1, list2):
    list1.sort()
    list2.sort()

    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    return total_distance

def get_similarity_score(list1, list2):
    similarity_score = 0
    for n in list1:
        multiplier = list2.count(n)
        similarity_score += multiplier * n
    return similarity_score


list_one, list_two = get_lists(SRC_FILE)

# part 1
print(get_total_distance(list_one, list_two))

# part 2
print(get_similarity_score(list_one, list_two))