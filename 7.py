RECURSION_RESULT: int = 0


def parse_input(path: str) -> list[list[int]]:
    result: list[list[int]] = []
    with open(path) as f:
        for line in f:
            first = line.split(":")
            r = [int(first[0])]
            r += [int(x) for x in first[1].split(" ")[1:]]
            result.append(r)

    return result


def is_correct(total: int, inp: list[int]) -> bool:
    if len(inp) == 0 and total == RECURSION_RESULT:
        return True

    if len(inp) == 0 and total != RECURSION_RESULT:
        return False

    return (
        is_correct(total + inp[0], inp[1:])
        or is_correct(total * inp[0], inp[1:])
        or is_correct(int(str(total) + str(inp[0])), inp[1:])
    )


def count_corrects(inp: list[list[int]]) -> int:
    total = 0

    for i in inp:
        global RECURSION_RESULT
        RECURSION_RESULT = i[0]
        if is_correct(i[1], i[2:]):
            print("Currect: ", i[0])
            total += i[0]

    return total


def main():
    inp = parse_input("7_input.txt")

    print(inp)

    print("Part 1: ", count_corrects(inp))


main()
