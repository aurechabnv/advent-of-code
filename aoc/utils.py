from time import perf_counter


def benchmark(title: str, function: callable):
    """
    Execute and benchmark a function
    :param title:
    :param function:
    :return:
    """
    start_time = perf_counter()
    result = function()
    end_time = perf_counter()
    print(f"{title}{' ' * (10 - len(title))} \t Time: {end_time - start_time:.4f} \t Result: {result}")


def init_grid(data: str, process_value: callable = None) -> dict:
    if not process_value:
        process_value = lambda x: x
    return {(y, x): process_value(v) for y, l in enumerate(data.splitlines()) for x, v in enumerate(l)}


def print_grid(grid: dict, process_value: callable = None):
    if not process_value:
        process_value = lambda x: x
    array = []
    for (y, x), value in grid.items():
        if y >= len(array):
            array.append([])
        array[y].append(process_value(value))
    print('\n'.join(''.join(line) for line in array))
