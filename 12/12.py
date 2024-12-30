from queue import Queue

VISITED: set[tuple[int, int]] = set()


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return [l.split("\n")[0] for l in f.readlines()]


def calculate_area_cost(mat: list[str], start: tuple[int, int]) -> int:
    to_visit: Queue[tuple[int, int]] = Queue()
    area = 0
    perimeter = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    plant_type = mat[start[0]][start[1]]
    to_visit.put(start)
    VISITED.add(start)

    while not to_visit.empty():
        neighbor = to_visit.get()

        area += 1

        # calculate perimeter
        for perimeter_dir in directions:
            x = neighbor[0] + perimeter_dir[0]
            y = neighbor[1] + perimeter_dir[1]

            if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] != plant_type:
                perimeter += 1
            if not (0 <= x < len(mat)):
                perimeter += 1
            if not (0 <= y < len(mat[0])):
                perimeter += 1

        for direction in directions:
            i = neighbor[0] + direction[0]
            j = neighbor[1] + direction[1]

            if (
                (i, j) not in VISITED
                and 0 <= i < len(mat)
                and 0 <= j < len(mat[0])
                and mat[i][j] == plant_type
            ):
                to_visit.put((i, j))
                VISITED.add((i, j))

    return area * perimeter


def calculate_total_cost(mat: list[str]) -> int:
    total = 0

    for i, line in enumerate(mat):
        for j, _ in enumerate(line):
            if (i, j) not in VISITED:
                cost = calculate_area_cost(mat, (i, j))
                print(cost)
                total += cost

    return total


# PART 2
def calculate_area_cost_with_side(mat: list[str], start: tuple[int, int]) -> int:
    to_visit: Queue[tuple[int, int]] = Queue()
    area = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    plant_type = mat[start[0]][start[1]]
    to_visit.put(start)
    VISITED.add(start)

    print("New", start)

    fences: list[tuple[int, int]] = []

    while not to_visit.empty():
        neighbor = to_visit.get()

        area += 1

        # calculate perimeter
        for perimeter_dir in directions:
            x = neighbor[0] + perimeter_dir[0]
            y = neighbor[1] + perimeter_dir[1]

            if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] != plant_type:
                fences.append((x, y))
            if not (0 <= x < len(mat)):
                fences.append((x, y))
            if not (0 <= y < len(mat[0])):
                fences.append((x, y))

        for direction in directions:
            i = neighbor[0] + direction[0]
            j = neighbor[1] + direction[1]

            if (
                (i, j) not in VISITED
                and 0 <= i < len(mat)
                and 0 <= j < len(mat[0])
                and mat[i][j] == plant_type
            ):
                to_visit.put((i, j))
                VISITED.add((i, j))

    fences.sort(key=lambda x: x[0])

    print("before:", fences)
    i = 0
    while i < len(fences) - 1:
        if (
            fences[i][0] == fences[i + 1][0]
            and abs(fences[i][1] - fences[i + 1][1]) == 1
        ):
            print("removing", fences[i])
            fences.remove(fences[i])
        else:
            i += 1

    print("after:", fences)
    print()

    fences.sort(key=lambda x: x[1])
    print("Sorteed", fences)
    i = 0
    while i < len(fences) - 1:
        if (
            fences[i][1] == fences[i + 1][1]
            and abs(fences[i][0] - fences[i + 1][0]) == 1
        ):
            print("removing", fences[i])
            fences.remove(fences[i])
        else:
            i += 1
    print("after", fences)
    print()

    return area * len(fences)


def calculate_total_cost_using_side(mat: list[str]) -> int:
    total = 0

    for i, line in enumerate(mat):
        for j, _ in enumerate(line):
            if (i, j) not in VISITED:
                cost = calculate_area_cost_with_side(mat, (i, j))
                total += cost

    return total


def main():
    mat = parse_input("12_input.txt")
    print(mat)
    # print("Part 1: ", calculate_total_cost(mat))a
    print("Part 2: ", calculate_total_cost_using_side(mat))


main()
