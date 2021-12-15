from typing import List, Tuple
from timeit import timeit
from collections import defaultdict


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> Tuple:
    lines = read_file(file_name)
    split = lines.index("")
    points = list(map(lambda y: [int(y[0]), int(y[1])], list(map(lambda x: x.split(","), lines[:split]))))
    folds = list(map(lambda x: (x[11], int(x[13:])), lines[split + 1:]))
    return points, folds


def fold(points, axes, line):
    axes = 0 if axes == 'x' else 1
    for p in points:
        if p[axes] > line:
            p[axes] = line - abs(p[axes] - line)
    return points


def exercise1(data: Tuple) -> int:
    points = data[0]
    folds = data[1]
    fold(points, folds[0][0], folds[0][1])
    counts = defaultdict(int)
    for p in points:
        counts[(p[0], p[1])] = 1
    return len(counts)


def exercise2(data: Tuple) -> int:
    points = data[0]
    folds = data[1]
    for f in folds:
        fold(points, f[0], f[1])
    max_x = max([x[0] for x in points])
    max_y = max([y[1] for y in points])

    for y in range(max_y+1):
        for x in range(max_x+1):
            s = u"\u2588" if [x, y] in points else ' '
            print(s, end='')
        print()
    print()
    return 0


if __name__ == "__main__":
    test_data = get_data("example_data")
    test_solution = read_file("example_solution")
    assert exercise1(test_data) == int(test_solution[0])
    assert exercise2(test_data) == int(test_solution[1])

    puzzle_input = get_data("data")
    print(f"Part 1: {exercise1(puzzle_input)}, Timing: %.2f ms" %
          (1000 * timeit(lambda: exercise1(puzzle_input), number=1)))
    print(f"Part 2: Timing: %.2f ms" %
          (1000 * timeit(lambda: exercise2(puzzle_input), number=1)))
