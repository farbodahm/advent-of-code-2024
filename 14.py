import re


mat = [[0] * 101 for _ in range(103)]


def parse_input(path: str) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

    positions: list[tuple[int, int]] = []
    velocities: list[tuple[int, int]] = []

    with open(path) as f:
        for line in f:
            groups = re.findall(pattern, line)[0]

            positions.append((int(groups[1]), int(groups[0])))
            velocities.append((int(groups[3]), int(groups[2])))

    return (positions, velocities)


def calculate_safety_factor() -> int:
    part1 = 0
    part2 = 0
    part3 = 0
    part4 = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == len(mat) // 2 or j == len(mat[0]) // 2:
                continue

            if 0 <= i < len(mat) // 2:
                if 0 <= j < len(mat[0]) // 2:
                    part1 += mat[i][j]
                else:
                    part2 += mat[i][j]
            else:
                if 0 <= j < len(mat[0]) // 2:
                    part3 += mat[i][j]
                else:
                    part4 += mat[i][j]

    return part1 * part2 * part3 * part4


def place_bot_on_map(p: tuple[int, int], v: tuple[int, int], sec: int) -> None:
    i, j = p

    for _ in range(sec):
        i = (i + v[0]) % len(mat)
        j = (j + v[1]) % len(mat[0])

    mat[i][j] += 1


def count_bots(ps: list[tuple[int, int]], vs: list[tuple[int, int]], sec: int) -> int:
    for p, v in zip(ps, vs):
        place_bot_on_map(p, v, sec)

    return calculate_safety_factor()


def main():
    positions, velocities = parse_input("./14_input.txt")

    print("Part 1: ", count_bots(positions, velocities, 100))


main()
