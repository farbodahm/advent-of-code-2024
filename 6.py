def read_input(path: str) -> list[str]:
    with open(path) as f:
        return f.readlines()


def find_starting_point(mat: list[str]) -> tuple[int, int, str]:
    shapes = {"^", ">", "v", "<"}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] in shapes:
                return (i, j, mat[i][j])

    return (-1, -1, "")


def count_tiles(mat) -> int:
    i, j, shape = find_starting_point(mat)
    result: set[tuple[int, int]] = set()
    result.add((i, j))

    while 0 < i < len(mat) - 1 and 0 < j < len(mat[0]) - 1:
        match shape:
            case "^":
                if mat[i - 1][j] == "#":
                    shape = ">"
                    continue
                i -= 1
            case ">":
                if mat[i][j + 1] == "#":
                    shape = "v"
                    continue
                j += 1
            case "v":
                if mat[i + 1][j] == "#":
                    shape = "<"
                    continue
                i += 1
            case "<":
                if mat[i][j - 1] == "#":
                    shape = "^"
                    continue
                j -= 1
            case _:
                raise Exception("Unexpected shape")
        result.add((i, j))

    return len(result)


def main():
    mat = read_input("./6_input.txt")

    print("Part 1: ", count_tiles(mat))


main()
