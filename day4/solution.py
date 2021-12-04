from typing import List


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str):
    lines = read_file(file_name)
    numbers = lines[0].split(',')
    boards = [[]]
    board_number = 0
    for line in lines[2:]:
        if line == "":
            board_number += 1
            boards.append([])
        else:
            boards[board_number].append(list(map(int, line.split())))
    return numbers, boards


def exercise1(numbers: List[int], boards: List[List[List[int]]]) -> int:
    for n in numbers:
        for board in boards:
            pass
    return 0


def exercise2(puzzle_input: List[str]) -> int:
    return 1


if __name__ == "__main__":
    # test_data = get_data("example_data")
    # assert exercise1(test_data) == 198
    # assert exercise2(test_data) == 230

    data = get_data("data")
    print(f"Exercise 1: {exercise1(data)}")
    print(f"Exercise 2: {exercise2(data)}")
