from collections import defaultdict


def read_input(path: str) -> tuple[list[int], list[int]]:
    first: list[int] = []
    second: list[int] = []

    with open(path, "r") as f:
        for line in f:
            splitted = line.split()
            first.append(int(splitted[0]))
            second.append(int(splitted[1]))

    return (first, second)


def calculate_distances(first: list[int], second: list[int]) -> int:
    first.sort()
    second.sort()

    total = 0
    for f, s in zip(first, second):
        total += abs(f - s)

    return total


def calculate_similarity_score(first: list[int], second: list[int]) -> int:
    second_occurrences: dict[int, int] = defaultdict(int)

    for i in second:
        second_occurrences[i] += 1

    total = 0
    for i in first:
        total += i * second_occurrences[i]

    return total


def main():
    first, second = read_input("./1_input.txt")

    print("First Part: ", calculate_distances(first, second))
    print("Second Part: ", calculate_similarity_score(first, second))


main()
