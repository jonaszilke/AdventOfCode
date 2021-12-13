from typing import List
from timeit import timeit


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> List[str]:
    return read_file(file_name)


def exercise1(data: List[str]) -> int:
    points = {")": 3, "]": 57,  "}": 1197, ">": 25137}
    brackets = {"]": "[", ")": "(", "}": "{", ">": "<"}
    result = 0
    for line in data:
        stack = []
        for i in line:
            if i in brackets.values():
                stack.append(i)
            elif brackets[i] != stack.pop():
                result += points[i]
                break
    return result


def exercise2(data: List[str]) -> int:
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    brackets = {"]": "[", ")": "(", "}": "{", ">": "<"}
    result = []
    for line in data:
        stack = []
        corrupted = False
        line_result = 0
        for i in line:
            if i in brackets.values():
                stack.append(i)
            elif brackets[i] != stack.pop():
                corrupted = True
                break
        if not corrupted:
            for i in stack[::-1]:
                line_result = line_result * 5 + points[i]
            result.append(line_result)
    return sorted(result)[len(result) // 2]


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
