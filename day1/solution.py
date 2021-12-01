from typing import List


def get_data(file_name):
    with open(file_name, "r") as file:
        puzzle_input = file.read().splitlines()
        return list(map(int, puzzle_input))


def count_increases(puzzle_input: List[int], sliding_window: int) -> int:
    counter = 0
    previous_sum = sum(puzzle_input[:sliding_window])
    for i in range(1, len(puzzle_input) - sliding_window + 1):
        new_sum = sum(puzzle_input[i:i + sliding_window])
        counter += 1 if previous_sum < new_sum else 0
        previous_sum = new_sum
    return counter


def exercise1(puzzle_input: List[int]) -> int:
    return count_increases(puzzle_input, 1)


def exercise2(puzzle_input: List[int]) -> int:
    return count_increases(puzzle_input, 3)


if __name__ == "__main__":
    data = get_data("data")
    print(f"Exercise 1: {exercise1(data)}")
    print(f"Exercise 2: {exercise2(data)}")
