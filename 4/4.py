MAT: list[str]


def read_input(path: str) -> list[str]:
    with open(path) as f:
        return f.readlines()


def count_xmas_from_index(i: int, j: int) -> int:
    count = 0
    rows, cols = len(MAT), len(MAT[0])

    # Horizontal backwards
    if j >= 3:
        if MAT[i][j - 1] == "M" and MAT[i][j - 2] == "A" and MAT[i][j - 3] == "S":
            count += 1

    # Horizontal forward
    if j <= cols - 4:
        if MAT[i][j + 1] == "M" and MAT[i][j + 2] == "A" and MAT[i][j + 3] == "S":
            count += 1

    # Vertical upwards
    if i >= 3:
        if MAT[i - 1][j] == "M" and MAT[i - 2][j] == "A" and MAT[i - 3][j] == "S":
            count += 1

    # Vertical downwards
    if i <= rows - 4:
        if MAT[i + 1][j] == "M" and MAT[i + 2][j] == "A" and MAT[i + 3][j] == "S":
            count += 1

    # Diagonal upwards right
    if i >= 3 and j <= cols - 4:
        if (
            MAT[i - 1][j + 1] == "M"
            and MAT[i - 2][j + 2] == "A"
            and MAT[i - 3][j + 3] == "S"
        ):
            count += 1

    # Diagonal upwards left
    if i >= 3 and j >= 3:
        if (
            MAT[i - 1][j - 1] == "M"
            and MAT[i - 2][j - 2] == "A"
            and MAT[i - 3][j - 3] == "S"
        ):
            count += 1

    # Diagonal downwards right
    if i <= rows - 4 and j <= cols - 4:
        if (
            MAT[i + 1][j + 1] == "M"
            and MAT[i + 2][j + 2] == "A"
            and MAT[i + 3][j + 3] == "S"
        ):
            count += 1

    # Diagonal downwards left
    if i <= rows - 4 and j >= 3:
        if (
            MAT[i + 1][j - 1] == "M"
            and MAT[i + 2][j - 2] == "A"
            and MAT[i + 3][j - 3] == "S"
        ):
            count += 1

    return count


def count_x_mas_from_index(i: int, j: int) -> int:
    count = 0
    rows, cols = len(MAT), len(MAT[0])

    if i - 1 >= 0 and i + 1 < rows and j - 1 >= 0 and j + 1 < cols:
        # Pattern 1: M.M / .A. / S.S
        if (
            MAT[i - 1][j + 1] == "M"
            and MAT[i - 1][j - 1] == "M"
            and MAT[i + 1][j - 1] == "S"
            and MAT[i + 1][j + 1] == "S"
        ):
            count += 1

        # Pattern 2: S.S / .A. / M.M
        if (
            MAT[i - 1][j + 1] == "S"
            and MAT[i - 1][j - 1] == "S"
            and MAT[i + 1][j - 1] == "M"
            and MAT[i + 1][j + 1] == "M"
        ):
            count += 1

        # Pattern 3: M.S / .A. / M.S
        if (
            MAT[i - 1][j + 1] == "S"
            and MAT[i - 1][j - 1] == "M"
            and MAT[i + 1][j - 1] == "M"
            and MAT[i + 1][j + 1] == "S"
        ):
            count += 1

        # Pattern 4: S.M / .A. / S.M
        if (
            MAT[i - 1][j + 1] == "M"
            and MAT[i - 1][j - 1] == "S"
            and MAT[i + 1][j - 1] == "S"
            and MAT[i + 1][j + 1] == "M"
        ):
            count += 1

    return count


def calculate_xmas() -> int:
    total = 0
    for i in range(len(MAT)):
        for j in range(len(MAT[i])):
            if MAT[i][j] == "X":
                total += count_xmas_from_index(i, j)

    return total


def calculate_x_mas() -> int:
    total = 0

    for i in range(len(MAT)):
        for j in range(len(MAT[i])):
            if MAT[i][j] == "A":
                total += count_x_mas_from_index(i, j)

    return total


def main():
    global MAT
    MAT = read_input("4_input.txt")

    print("Part 1: ", calculate_xmas())
    print("Part 2: ", calculate_x_mas())


main()
