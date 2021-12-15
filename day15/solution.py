from typing import List, Tuple
from timeit import timeit
from collections import defaultdict
from copy import deepcopy


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> List[List[int]]:
    return [list(map(int, x)) for x in read_file(file_name)]


def get_neighbors(data, i, j):
    return [(x, y) for x, y in [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)] if
            0 <= x < len(data) and 0 <= y < len(data[0])]


def get_min(cost_map, points):
    min_point = points[0]
    for p in points[1:]:
        if cost_map[p] < cost_map[min_point]:
            min_point = p
    return min_point


def exercise1(data: List[List[int]]) -> int:
    start = (0, 0)
    end = (len(data) - 1, len(data) - 1)
    new_points = [start]
    cost_map = defaultdict(lambda: -1)
    cost_map[(0, 0)] = 0

    while new_points:
        min_point = get_min(cost_map, new_points)
        if cost_map[end] != -1 and cost_map[min_point] > cost_map[end]:
            return cost_map[end]
        new_points.remove(min_point)
        neighbors = get_neighbors(data, min_point[0], min_point[1])
        for n in neighbors:
            if cost_map[n] == -1:
                cost_map[n] = cost_map[min_point] + data[n[0]][n[1]]
                new_points.append(n)
            elif cost_map[n] > cost_map[min_point] + data[n[0]][n[1]]:
                cost_map[n] = cost_map[min_point] + data[n[0]][n[1]]
                new_points.append(n)
    return cost_map[end]


def exercise2(data: List[List[int]]) -> int:
    new_data = deepcopy(data)
    for d in range(len(data)):
        for i in range(1, 5):
            new_data[d] += list(map(lambda x: x + i if x + i < 10 else x + i - 9, data[d]))
    for i in range(1, 5):
        for d in range(len(data)):
            new_data.append(list(map(lambda x: x + i if x + i < 10 else x + i - 9, new_data[d])))
    return exercise1(new_data)


if __name__ == "__main__":
    test_data = get_data("example_data")
    test_solution = read_file("example_solution")
    assert exercise1(test_data) == int(test_solution[0])
    assert exercise2(test_data) == int(test_solution[1])

    puzzle_input = get_data("data")
    print(f"Part 1: {exercise1(puzzle_input)}, Timing: %.2f ms" %
          (1000 * timeit(lambda: exercise1(puzzle_input), number=1)))
    print(f"Part 2: {exercise2(puzzle_input)}, Timing: %.2f ms" %
          (1000 * timeit(lambda: exercise2(puzzle_input), number=1)))
