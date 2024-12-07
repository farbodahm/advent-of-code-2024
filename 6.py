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


def count_tiles(mat: list[str]) -> set[tuple[int, int]]:
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

    return result


def is_in_loop(mat: list[list[str]], position: tuple[int, int], shape: str) -> bool:
    i, j = position
    visited: set[tuple[int, int, str]] = set()

    while 0 < i < len(mat) - 1 and 0 < j < len(mat[0]) - 1:
        visited.add((i, j, shape))

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

        if (i, j, shape) in visited:
            return True

    return False


def count_obstacle_to_create_loop(
    mat: list[str], visiting: set[tuple[int, int]]
) -> int:
    total = 0
    start_i, start_j, shape = find_starting_point(mat)
    visiting.remove((start_i, start_j))

    # Convert mat to a list of lists for mutability
    mutable_mat = [list(row) for row in mat]

    for i, j in visiting:
        mutable_mat[i][j] = "#"
        if is_in_loop(mutable_mat, (start_i, start_j), shape):
            total += 1
        mutable_mat[i][j] = "."

    # Convert mutable_mat back to the original format if needed
    return total


def main():
    mat = read_input("./6_input.txt")
    visited_tiles = count_tiles(mat)

    print(visited_tiles)
    print("Part 1: ", len(visited_tiles))
    print("Part 2: ", count_obstacle_to_create_loop(mat, visited_tiles))


main()
