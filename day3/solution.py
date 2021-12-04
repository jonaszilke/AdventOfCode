from typing import List


def get_data(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def exercise1(puzzle_input: List[str]) -> int:
    gamma = ""
    epsilon = ""
    for i in range(len(puzzle_input[0])):
        zeros = 0
        ones = 0
        for j in range(len(puzzle_input)):
            if puzzle_input[j][i] == '1':
                ones += 1
            else:
                zeros += 1
        gamma += "1" if zeros < ones else "0"
        epsilon += "0" if zeros < ones else "1"
    print(gamma)
    g = int(gamma, 2)
    e = int(epsilon, 2)
    return g * e


def exercise2(puzzle_input: List[str]) -> int:
    return calculate(puzzle_input, "ox")*calculate(puzzle_input, "co2")


def calculate(puzzle_input: List[str], mode: str = "ox"):
    m = ['0', '1'] if mode == "co2" else ['1', '0']
    co2_list = puzzle_input.copy()
    i = 0
    while len(co2_list) > 1:
        zeros = 0
        ones = 0
        for j in range(len(co2_list)):
            if co2_list[j][i] == '1':
                ones += 1
            else:
                zeros += 1
        if zeros <= ones:
            co2_list = [x for x in co2_list if x[i] == m[0]]
        else:
            co2_list = [x for x in co2_list if x[i] == m[1]]
        i += 1
    return int(co2_list[0], 2)


if __name__ == "__main__":
    test_data = get_data("example_data")
    assert exercise1(test_data) == 198
    assert exercise2(test_data) == 230

    data = get_data("data")
    print(f"Exercise 1: {exercise1(data)}")
    print(f"Exercise 2: {exercise2(data)}")
