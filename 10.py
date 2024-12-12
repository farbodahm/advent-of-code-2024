import queue


def read_input(path: str) -> list[str]:
    with open(path) as f:
        return [l.split()[0] for l in f.readlines()]


def find_starting_points(mat: list[str]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []

    for i, line in enumerate(mat):
        for j, char in enumerate(line):
            if char == "0":
                result.append((i, j))

    return result


def calculate_score(mat: list[str], starting_point: tuple[int, int]) -> int:
    accepted_points: set[tuple[int, int]] = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    to_visit: queue.Queue[tuple[int, int]] = queue.Queue()
    visited: set[tuple[int, int]] = set()
    to_visit.put(starting_point)

    while not to_visit.empty():
        current = to_visit.get()
        visited.add(current)

        if mat[current[0]][current[1]] == "9":
            print("Accepted", current)
            accepted_points.add(current)

        for dir in directions:
            i = current[0] + dir[0]
            j = current[1] + dir[1]
            new = (i, j)
            if (
                new not in visited
                and 0 <= i < len(mat)
                and 0 <= j < len(mat[0])
                and mat[i][j] != "."
                and (int(mat[i][j]) - int(mat[current[0]][current[1]])) == 1
            ):
                to_visit.put(new)

    return len(accepted_points)


def calculate_score_distinct(mat: list[str], starting_point: tuple[int, int]) -> int:
    accepted_points = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    to_visit: queue.Queue[tuple[int, int]] = queue.Queue()
    visited: set[tuple[int, int]] = set()
    to_visit.put(starting_point)

    while not to_visit.empty():
        current = to_visit.get()
        visited.add(current)

        if mat[current[0]][current[1]] == "9":
            print("Accepted", current)
            accepted_points += 1
            continue

        for dir in directions:
            i = current[0] + dir[0]
            j = current[1] + dir[1]
            new = (i, j)
            if (
                new not in visited
                and 0 <= i < len(mat)
                and 0 <= j < len(mat[0])
                and mat[i][j] != "."
                and (int(mat[i][j]) - int(mat[current[0]][current[1]])) == 1
            ):
                to_visit.put(new)

    return accepted_points


def calculate_total_score(
    mat: list[str], starting_points: list[tuple[int, int]]
) -> int:
    total = 0

    for start_point in starting_points:
        total += calculate_score(mat, start_point)

    return total


def calculate_total_score_distinct(
    mat: list[str], starting_points: list[tuple[int, int]]
) -> int:
    total = 0

    for start_point in starting_points:
        total += calculate_score_distinct(mat, start_point)

    return total


def main():
    mat = read_input("10_input.txt")
    starting_points = find_starting_points(mat)
    print("Part 1: ", calculate_total_score(mat, starting_points))
    print("Part 2: ", calculate_total_score_distinct(mat, starting_points))


main()
