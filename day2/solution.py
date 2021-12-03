from typing import List


def get_data(file_name: str) -> List[list]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
        puzzle_input = list(map(lambda x: x.split(), lines))
        return puzzle_input


def exercise1(puzzle_input: List[list]) -> int:
    horizontal, depth = 0, 0
    for i in puzzle_input:
        if i[0] == 'forward':
            horizontal += int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
        elif i[0] == 'up':
            depth -= int(i[1])
    return horizontal * depth


def exercise2(puzzle_input: List[list]) -> int:
    horizontal, depth, aim = 0, 0, 0
    for i in puzzle_input:
        if i[0] == 'forward':
            horizontal += int(i[1])
            depth += aim * int(i[1])
        elif i[0] == 'down':
            aim += int(i[1])
        elif i[0] == 'up':
            aim -= int(i[1])
    return horizontal * depth


if __name__ == "__main__":
    data = get_data("data")
    print(f"Exercise 1: {exercise1(data)}")
    print(f"Exercise 2: {exercise2(data)}")
