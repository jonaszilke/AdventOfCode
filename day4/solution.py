from typing import List


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str):
    lines = read_file(file_name)
    numbers = list(map(int, lines[0].split(',')))
    boards = [[]]
    board_number = 0
    for line in lines[2:]:
        if line == "":
            board_number += 1
            boards.append([])
        else:
            boards[board_number].append(list(map(int, line.split())))
    return numbers, boards


def is_finished(numbers, board):
    for row in board:
        if all(item in numbers for item in row):
            return True
    for column in list(map(list, zip(*board))):
        if all(item in numbers for item in column):
            return True
    return False


def find_first_board(numbers: List[int], boards: List[List[List[int]]]):
    for i in range(1, len(numbers)):
        for board in boards:
            if is_finished(numbers[:i], board):
                return numbers[:i], board


def exercise1(numbers: List[int], boards: List[List[List[int]]]) -> int:
    used_numbers, board = find_first_board(numbers, boards)
    for num in used_numbers:
        for row in board:
            if num in row:
                row.remove(num)
    return sum(sum(board, [])) * used_numbers[-1]


def find_last_board(numbers: List[int], boards: List[List[List[int]]]):
    cboards = boards.copy()
    i = 1
    while len(cboards) > 1:
        finished = []
        for b in cboards:
            if is_finished(numbers[:i], b):
                finished.append(b)
        for b in finished:
            cboards.remove(b)
        i += 1
    return numbers[:i], cboards[0]


def exercise2(numbers: List[int], boards: List[List[List[int]]]) -> int:
    used_numbers, board = find_last_board(numbers, boards)
    for num in used_numbers:
        for row in board:
            if num in row:
                row.remove(num)
    return sum(sum(board, [])) * used_numbers[-1]


if __name__ == "__main__":
    numbers, boards = get_data("example_data")
    assert exercise1(numbers, boards) == 4512
    assert exercise2(numbers, boards) == 1924
    numbers, boards = get_data("data")
    print(f"Exercise 1: {exercise1(numbers, boards)}")
    print(f"Exercise 2: {exercise2(numbers, boards)}")
