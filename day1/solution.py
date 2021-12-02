from typing import List


def get_data(file_name: str) -> List[int]:
    with open(file_name, "r") as f:
        puzzle_input = f.read().splitlines()
        return list(map(int, puzzle_input))


def count_increases(puzzle_input: List[int], sliding_window: int) -> int:
    summed_list = [sum(puzzle_input[i:i + sliding_window])
                   for i in range(len(puzzle_input) - sliding_window + 1)]
    return sum(map(lambda x: x[0] < x[1], zip(summed_list[:-1], summed_list[1:])))


def exercise1(puzzle_input: List[int]) -> int:
    return count_increases(puzzle_input, 1)


def exercise2(puzzle_input: List[int]) -> int:
    return count_increases(puzzle_input, 3)


if __name__ == "__main__":
    data = get_data("data")
    print(f"Exercise 1: {exercise1(data)}")
    print(f"Exercise 2: {exercise2(data)}")
