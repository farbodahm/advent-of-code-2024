import heapq


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return [l.split()[0] for l in f.readlines()]


def find_starting(mat: list[str]) -> tuple[int, int]:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "S":
                return (i, j)
    return (-1, -1)


def find_minimum_cost(mat: list[str], start: tuple[int, int]) -> int:
    dirs = [
        (1, 0, "v"),
        (0, 1, ">"),
        (-1, 0, "^"),
        (0, -1, "<"),
    ]

    # Priority queue for Dijkstra: (cost, x, y, direction)
    pq: list[tuple[int, int, int, str]] = []
    heapq.heappush(pq, (0, start[0], start[1], ">"))

    # Keep track of the minimum cost to each cell for each direction
    min_cost = {}
    min_cost[(start[0], start[1], ">")] = 0

    while pq:
        cost, i, j, pos = heapq.heappop(pq) # Dijkstra Guarantees that this is the cheapest way to visit this node.

        # If we've reached the end, return the cost
        if mat[i][j] == "E":
            return cost

        # Explore neighbors
        for dx, dy, new_pos in dirs:
            new_i, new_j = i + dx, j + dy

            if (
                0 <= new_i < len(mat)
                and 0 <= new_j < len(mat[0])
                and mat[new_i][new_j] != "#"
            ):
                # Calculate the cost of moving
                new_cost = cost + (1 if pos == new_pos else 1001)

                # If this path is cheaper, consider it
                if (new_i, new_j, new_pos) not in min_cost or new_cost < min_cost[
                    (new_i, new_j, new_pos)
                ]:
                    min_cost[(new_i, new_j, new_pos)] = new_cost
                    heapq.heappush(pq, (new_cost, new_i, new_j, new_pos))

    return -1


def main():
    mat = parse_input("./16_input.txt")

    for l in mat:
        print(l)

    start = find_starting(mat)

    print("Start:", start)

    print("Part 1: Minimum Cost = ", find_minimum_cost(mat, start))


main()
