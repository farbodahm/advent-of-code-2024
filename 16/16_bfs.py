from queue import Queue


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return [l.split()[0] for l in f.readlines()]


def find_starting(mat: list[str]) -> tuple[int, int]:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "S":
                return (i, j)
    return (-1, -1)


def find_end(mat: list[str]) -> tuple[int, int]:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "E":
                return (i, j)
    return (-1, -1)


def find_all_costs(
    mat: list[str], start: tuple[int, int], end: tuple[int, int]
) -> list[int]:
    accepted: list[int] = []
    to_visit: Queue[tuple[int, int, int, str]] = Queue()
    min_cost: dict[tuple[int, int, str], int] = {}
    dirs = [
        (1, 0, "v"),
        (0, 1, ">"),
        (-1, 0, "^"),
        (0, -1, "<"),
    ]

    i, j = start
    pos: str = ">"
    cost: int = 0
    to_visit.put((i, j, cost, pos))
    min_cost[(i, j, pos)] = cost

    while not to_visit.empty():
        i, j, cost, pos = to_visit.get()

        if (i, j) == end:
            accepted.append(cost)
            continue

        for dir in dirs:
            new_i = i + dir[0]
            new_j = j + dir[1]
            new_pos = dir[2]

            if (
                0 <= new_i < len(mat)
                and 0 <= new_j < len(mat[0])
                and mat[new_i][new_j] != "#"
            ):
                new_cost = cost + (1 if pos == new_pos else 1001)

                # Only explore if this path offers a lower cost
                if (new_i, new_j, new_pos) not in min_cost or new_cost < min_cost[
                    (new_i, new_j, new_pos)
                ]:
                    min_cost[(new_i, new_j, new_pos)] = new_cost
                    to_visit.put((new_i, new_j, new_cost, new_pos))

    return accepted


def main():
    mat = parse_input("./16_input.txt")

    start = find_starting(mat)
    end = find_end(mat)

    all_costs = find_all_costs(mat, start, end)
    print("All Costs:", all_costs)
    print("Minimum Cost:", min(all_costs))


main()
