from queue import Queue

N = 71
MAT: list[list[str]] = [["."] * N for _ in range(N)]


def parse_input(path: str) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []
    with open(path) as f:
        for l in f:
            j, i = l.split(",")
            res.append((int(i), int(j)))
    return res[:1024]


def draw_map(obstacles: list[tuple[int, int]]) -> None:
    for obs in obstacles:
        MAT[obs[0]][obs[1]] = "#"


def count_steps() -> int:
    end = (N - 1, N - 1)
    path: dict[tuple[int, int], tuple[int, int]] = {}
    to_visit: Queue[tuple[int, int]] = Queue()
    i, j = 0, 0
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    to_visit.put((i, j))

    while not to_visit.empty():
        i, j = to_visit.get()

        if (i, j) == end:
            current = (i, j)
            total = 0
            while current != (0, 0):
                current = path[current]
                total += 1
            return total

        for dx, dy in dirs:
            new_i = i + dx
            new_j = j + dy

            if (
                0 <= new_i < N
                and 0 <= new_j < N
                and MAT[new_i][new_j] != "#"
                and (new_i, new_j) not in path
            ):
                to_visit.put((new_i, new_j))
                path[(new_i, new_j)] = (i, j)

    return -1


def main():
    obstacles = parse_input("./18_input.txt")
    draw_map(obstacles)

    print("Part 1: ", count_steps())


main()
