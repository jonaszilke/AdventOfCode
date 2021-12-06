from typing import List, Dict
from collections import Counter


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> Dict[int, int]:
    data = dict(Counter(list(map(int, read_file(file_name)[0].split(',')))))
    for i in range(9):
        if i not in data.keys():
            data[i] = 0
    return data


def day(data: Dict[int, int]):
    tmp = data[0]
    for d in range(8):
        data[d] = data[d + 1]
    data[8] = tmp
    data[6] += tmp


def exercise1(data: Dict[int, int]) -> int:
    for i in range(80):
        day(data)
    return sum(data.values())


def exercise2(data: Dict[int, int]) -> int:
    for i in range(256):
        day(data)
    return sum(data.values())


if __name__ == "__main__":
    test_data = get_data("example_data")
    test_solution = read_file("example_solution")

    assert exercise1(test_data.copy()) == int(test_solution[0])
    assert exercise2(test_data.copy()) == int(test_solution[1])

    data = get_data("data")
    print(f"Exercise 1: {exercise1(data.copy())}")
    print(f"Exercise 2: {exercise2(data.copy())}")
