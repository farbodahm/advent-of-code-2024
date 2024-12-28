AVAIL: frozenset[str]
EXPECTED: str


def parse_input(path: str) -> tuple[set[str], list[str]]:
    avail: set[str] = set()
    expected: list[str] = []
    is_reading_avail = True

    with open(path) as f:
        for l in f:
            if l == "\n":
                is_reading_avail = False
                continue

            if is_reading_avail:
                avail = avail.union(set(l.split("\n")[0].split(", ")))
            else:
                expected.append(l.split()[0])

    return (avail, expected)


def can_create(i: int, l: str) -> bool:
    if i >= len(EXPECTED):
        return l in AVAIL

    if l not in AVAIL:
        return can_create(i + 1, l + EXPECTED[i])

    return can_create(i + 1, l + EXPECTED[i]) or can_create(i, "")


def count_towels(expected: list[str]) -> int:
    global EXPECTED
    total = 0
    for e in expected:
        EXPECTED = e
        if can_create(0, ""):
            total += 1
    return total


def main():
    global AVAIL
    AVAIL, expected = parse_input("./19_input.txt")

    print("Part 1: ", count_towels(expected))


main()
