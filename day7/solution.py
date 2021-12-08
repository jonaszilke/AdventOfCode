from typing import List


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> List[int]:
    return list(map(int, read_file(file_name)[0].split(',')))


def calculate(data: List[int], dist):
    fuel = []
    for i in range(max(data)):
        fuel.append(dist(i))
    return min(fuel)


def exercise1(data: List[int]) -> int:
    dist = lambda pos: sum([abs(x - pos) for x in data])
    return calculate(data, dist)


def exercise2(data: List[int]) -> int:
    dist = lambda pos: sum(list(map(lambda x: int((x * (x + 1)) / 2), [abs(x - pos) for x in data])))
    return calculate(data, dist)


if __name__ == "__main__":
    test_data = get_data("example_data")
    test_solution = read_file("example_solution")
    assert exercise1(test_data) == int(test_solution[0])
    assert exercise2(test_data) == int(test_solution[1])

    puzzle_input = get_data("data")
    print(f"Exercise 1: {exercise1(puzzle_input)}")
    print(f"Exercise 2: {exercise2(puzzle_input)}")
