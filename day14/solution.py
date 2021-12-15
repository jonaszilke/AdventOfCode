from typing import List, Tuple, Dict
from timeit import timeit
from collections import defaultdict


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> Tuple:
    lines = read_file(file_name)
    rules = list(map(lambda x: x.split(" -> "), lines[2:]))
    rules_dict = {}
    for r in rules:
        rules_dict[r[0]] = r[1]
    return lines[0], rules_dict


def step(chain: defaultdict, rules: Dict):
    new_chain = defaultdict(int)
    for k, v in chain.items():
        if k in rules:
            new_chain[k[0] + rules[k]] += v
            new_chain[rules[k] + k[1]] += v
        else:
            new_chain[k] += v
    return new_chain


def solve(data, times):
    start = data[0]
    rules = data[1]
    chain = defaultdict(int)
    for i in range(len(start) - 1):
        chain[start[i:i + 2]] += 1
    for i in range(times):
        chain = step(chain, rules)
    counts = defaultdict(int)
    counts[start[0]] += 1
    counts[start[-1]] += 1
    for c in chain.keys():
        counts[c[0]] += chain[c]
        counts[c[1]] += chain[c]
    result = (max(counts.values()) - min(counts.values())) // 2
    return result


def exercise1(data: Tuple) -> int:
    return solve(data, 10)


def exercise2(data: Tuple) -> int:
    return solve(data, 40)


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
