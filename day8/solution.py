from typing import List, Tuple, Set, Dict


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> List[Tuple[List[str], List[str]]]:
    return [(i[:-4], i[-4:]) for i in list(map(lambda s: s.replace(" | ", ' ').split(' '), read_file(file_name)))]


def exercise1(data: List[Tuple[List[str], List[str]]]) -> int:
    return len([1 for d in data for s in d[1] if len(s) in [2, 3, 4, 7]])


def find_connections(data: List[str]) -> Dict[int, Set[str]]:
    numbers = {}
    for s in data:
        if len(s) == 2:
            numbers[1] = set(s)
        elif len(s) == 3:
            numbers[7] = set(s)
        elif len(s) == 7:
            numbers[8] = set(s)
        elif len(s) == 4:
            numbers[4] = set(s)

    for s in data:
        if len(s) == 5:
            if (numbers[4] - numbers[7]).issubset(s):
                numbers[5] = set(s)
            elif numbers[1].issubset(s):
                numbers[3] = set(s)
            else:
                numbers[2] = set(s)
        if len(s) == 6:
            if numbers[4].issubset(s):
                numbers[9] = set(s)
            elif numbers[1].issubset(s):
                numbers[0] = set(s)
            else:
                numbers[6] = set(s)
    return numbers


def exercise2(data: List[Tuple[List[str], List[str]]]) -> int:
    numbers = []
    for line in data:
        con = find_connections(line[0])
        n = ""
        for a in line[1]:
            for key, value in con.items():
                if set(a) == value:
                    n += str(key)
        numbers.append(int(n))
    return sum(numbers)


if __name__ == "__main__":
    test_data = get_data("example_data")
    test_solution = read_file("example_solution")
    assert exercise1(test_data) == int(test_solution[0])
    assert exercise2(test_data) == int(test_solution[1])

    puzzle_input = get_data("data")
    print(f"Exercise 1: {exercise1(puzzle_input)}")
    print(f"Exercise 2: {exercise2(puzzle_input)}")
