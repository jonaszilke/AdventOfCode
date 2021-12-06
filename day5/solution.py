from typing import List, Tuple
import numpy as np


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str):
    lines = list(map(lambda s: s.replace(' -> ', ',').split(','), read_file(file_name)))
    lines = list(map(lambda x: list(map(int, x)), lines))
    field_size = max(list(map(max, lines))) + 1
    points = list(map(lambda x: ((x[0], x[1]), (x[2], x[3])), lines))
    return points, field_size


class Line:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int]):
        self._start = start
        self._end = end

    def get_points(self):
        if self._start[0] == self._end[0]:
            if self._start[1] < self._end[1]:
                points = [(self._start[0], x) for x in range(self._start[1], self._end[1] + 1)]
            else:
                points = [(self._start[0], x) for x in range(self._start[1], self._end[1] - 1, -1)]
        elif self._start[1] == self._end[1]:
            if self._start[0] < self._end[0]:
                points = [(x, self._start[1]) for x in range(self._start[0], self._end[0] + 1)]
            else:
                points = [(x, self._start[1]) for x in range(self._start[0], self._end[0] - 1, -1)]
        elif self._start[0] < self._end[0]:
            if self._start[1] < self._end[1]:
                points = [(self._start[0] + x, self._start[1] + x) for x in range(0, abs(self._end[0] - self._start[0]) + 1)]
            else:
                points = [(self._start[0] + x, self._start[1] - x) for x in range(0, abs(self._end[0] - self._start[0]) + 1)]
        elif self._start[0] > self._end[0]:
            if self._start[1] < self._end[1]:
                points = [(self._start[0] - x, self._start[1] + x) for x in range(0, abs(self._end[0] - self._start[0]) + 1)]
            else:
                points = [(self._start[0] - x, self._start[1] - x) for x in range(0, abs(self._end[0] - self._start[0]) + 1)]
        return points

    def __str__(self):
        return f"{self._start}, {self._end}: {self.get_points()}"


class Field:
    def __init__(self, field_size: int):
        self._field = np.zeros((field_size, field_size))

    def add_line(self, line: Line):
        for point in line.get_points():
            self._field[point] += 1

    def dangerous_zones(self) -> int:
        return sum([1 for x in self._field.flatten() if x > 1])


def exercise1(data, field_size) -> int:
    field = Field(field_size)
    for line in data:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            field.add_line(Line(line[0], line[1]))
    return field.dangerous_zones()


def exercise2(data, field_size) -> int:
    field = Field(field_size)
    for line in data:
        field.add_line(Line(line[0], line[1]))
    return field.dangerous_zones()


if __name__ == "__main__":
    test_data, test_field_size = get_data("example_data")
    test_solution = read_file("example_solution")

    assert exercise1(test_data, test_field_size) == int(test_solution[0])
    assert exercise2(test_data, test_field_size) == int(test_solution[1])

    data, field_size = get_data("data")
    print(field_size)
    print(f"Exercise 1: {exercise1(data, field_size)}")
    print(f"Exercise 2: {exercise2(data, field_size)}")
