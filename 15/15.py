MAT: list[list[str]]


def parse_input(path: str) -> tuple[list[str], str]:
    mat: list[str] = []
    moves: str = ""
    is_reading_map = True

    with open(path) as f:
        for l in f:
            if l == "\n":
                is_reading_map = False
                continue

            if is_reading_map:
                mat.append(l.split()[0])
            else:
                moves += l.split()[0]

    return (mat, moves)


def find_starting_position(mat: list[str]) -> tuple[int, int]:
    for i, l in enumerate(mat):
        j = l.find("@")
        if j != -1:
            return (i, j)

    return (-1, -1)


def move_object(loc: tuple[int, int], dir: str) -> bool:
    """Return True if we can move the given object in the given direction"""
    i, j = loc
    new_i = i
    new_j = j
    match dir:
        case "^":
            new_i = i - 1
        case ">":
            new_j = j + 1
        case "v":
            new_i = i + 1
        case "<":
            new_j = j - 1
        case _:
            raise Exception(f"Unexpected dir {dir}")

    if MAT[new_i][new_j] == ".":
        MAT[new_i][new_j] = "O"
        MAT[i][j] = "."
        return True

    if MAT[new_i][new_j] == "#":
        return False

    if move_object((new_i, new_j), dir):
        MAT[new_i][new_j] = "O"
        MAT[i][j] = "."
        return True

    return False


def apply_moves(moves: str, start: tuple[int, int]):
    global MAT
    i, j = start
    new_i = i
    new_j = j

    for move in moves:
        match move:
            case "^":
                new_i = i - 1
                new_j = j
            case ">":
                new_j = j + 1
                new_i = i
            case "v":
                new_i = i + 1
                new_j = j
            case "<":
                new_j = j - 1
                new_i = i
            case _:
                raise Exception(f"Unexpected move {move}")

        if MAT[new_i][new_j] == "#":
            continue

        if MAT[new_i][new_j] == "O" and not move_object((new_i, new_j), move):
            continue

        MAT[i][j] = "."
        MAT[new_i][new_j] = "@"
        i, j = new_i, new_j


def calculate_coordinates_sums() -> int:
    sum = 0

    for i in range(len(MAT)):
        for j in range(len(MAT[0])):
            if MAT[i][j] == "O":
                sum += (100 * i) + j

    return sum


def main():
    mat, moves = parse_input("./15_input.txt")
    start = find_starting_position(mat)
    global MAT
    MAT = [list(l) for l in mat]
    apply_moves(moves, start)

    print("Part 1: ", calculate_coordinates_sums())


main()
