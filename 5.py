from collections import defaultdict
from graphlib import TopologicalSorter


def get_dependencies(rules: dict[int, set[int]]) -> dict[int, set[int]]:
    deps: dict[int, set[int]] = defaultdict(set[int])

    for key, values in rules.items():
        for value in values:
            deps[value].add(key)

    return deps


def parse_input(path: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    rules: dict[int, set[int]] = defaultdict(set[int])
    updates: list[list[int]] = []
    first_section = True

    with open(path) as f:
        for l in f:
            if l == "\n":
                first_section = False
                continue
            if first_section:
                rule = l.split("|")
                rules[int(rule[0])].add(int(rule[1]))
            else:
                updates += [[int(x) for x in l.split(",")]]

    return (rules, updates)


def sum_unordered_after_correction(
    deps: dict[int, set[int]], updates: list[list[int]]
) -> int:
    total = 0

    for update in updates:
        update_set = set(update)
        sorted: TopologicalSorter = TopologicalSorter()
        for i in update:
            sorted.add(i, *deps[i].intersection(update_set))
        sorted_list = list(sorted.static_order())
        total += sorted_list[len(sorted_list) // 2]

    return total


def sum_correct_order(
    deps: dict[int, set[int]], updates: list[list[int]]
) -> tuple[int, list[list[int]]]:
    total = 0
    unordered_updates: list[list[int]] = []
    for update in updates:
        visited: set[int] = set()
        update_set = set(update)
        for i in update:
            available_deps = deps[i].intersection(update_set)
            if len(available_deps) == len(visited):
                visited.add(i)
            else:
                unordered_updates += [update]
                break

        # If true, then it's a valid update
        if len(visited) == len(update):
            total += update[len(update) // 2]

    return total, unordered_updates


def main():
    rules, updates = parse_input("5_input.txt")
    deps = get_dependencies(rules)
    answer, unordered_updates = sum_correct_order(deps, updates)
    print("Part 1: ", answer, unordered_updates)
    print("Part 2: ", sum_unordered_after_correction(deps, unordered_updates))


main()
