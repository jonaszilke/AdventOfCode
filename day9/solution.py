from typing import List
import numpy as np
from timeit import timeit


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> List[List[int]]:
    return [list(map(int, list(line))) for line in read_file(file_name)]


def get_neighbors(data, i, j):
    return [data[x][y] for x, y in [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)] if
            0 <= x < len(data) and 0 <= y < len(data[0])]


def exercise1(data: List[List[int]]) -> int:
    risk = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] < min(get_neighbors(data, i, j)):
                risk.append(data[i][j] + 1)
    return sum(risk)


def get_neighbors_pos(data, i, j):
    return [(x, y) for x, y in [(i, j - 1), (i - 1, j)] if
            0 <= x < len(data) and 0 <= y < len(data[0])]


def exercise2(data: List[List[int]]) -> int:
    basins = np.zeros(shape=(len(data), len(data[0])))
    con = [0]
    next_num = 1
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] < 9:
                a = list(set([basins[x][y] for x, y in get_neighbors_pos(data, i, j) if basins[x][y] != 0]))
                if len(a) == 0:
                    basins[i][j] = next_num
                    con.append(next_num)
                    next_num += 1
                elif len(a) == 1:
                    basins[i][j] = a[0]
                else:
                    basins[i][j] = min(a)
                    con[int(max(a))] = int(con[int(min(a))])
                    for x in range(len(con)):
                        if con[x] == int(max(a)):
                            con[x] = int(con[int(min(a))])

    for i in range(len(data)):
        for j in range(len(data[i])):
            basins[i][j] = con[int(basins[i][j])]
    (unique, counts) = np.unique(basins, return_counts=True)
    return int(np.prod(np.sort(counts[1:])[-3:]))


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
