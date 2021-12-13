from typing import List, Dict, Set
from timeit import timeit


def read_file(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_data(file_name: str) -> Dict[str, Set[str]]:
    connections = list(map(lambda x: x.split("-"), read_file(file_name)))
    caves = {}
    for c in connections:
        if c[0] not in caves:
            caves[c[0]] = set()
        if c[1] not in caves:
            caves[c[1]] = set()
        caves[c[0]].add(c[1])
        caves[c[1]].add(c[0])
    return caves


def double_visits(path: List[str]):
    return len([x for x in path if x.islower()]) > len(set([x for x in path if x.islower()]))


def expand(data: Dict[str, Set[str]], paths: List[List[str]], finished_path: List[List[str]], part2=False):
    new_path_list = []
    for l in paths:
        for neighbor in data[l[-1]]:
            if neighbor == 'start':
                pass
            elif neighbor == 'end':
                new_list = l.copy()
                new_list.append(neighbor)
                finished_path.append(new_list)
            elif neighbor.isupper() or neighbor not in l:
                new_list = l.copy()
                new_list.append(neighbor)
                new_path_list.append(new_list)
            elif part2 and not double_visits(l):
                new_list = l.copy()
                new_list.append(neighbor)
                new_path_list.append(new_list)
    return new_path_list


def exercise1(data: Dict[str, Set[str]]) -> int:
    path_list = [['start']]
    finished_paths = []
    while path_list:
        path_list = expand(data, path_list, finished_paths)
    return len(finished_paths)


def exercise2(data: Dict[str, Set[str]]) -> int:
    path_list = [['start']]
    finished_paths = []
    while path_list:
        path_list = expand(data, path_list, finished_paths, True)
    return len(finished_paths)


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
