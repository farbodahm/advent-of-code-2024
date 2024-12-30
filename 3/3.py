import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
mul_with_instructions_pattern = r"don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\)"
do = True


def calculate_muls_per_line(line: str) -> int:
    muls = re.findall(mul_pattern, line)
    muls = [(int(mul[0]), int(mul[1])) for mul in muls]
    return sum([mul[0] * mul[1] for mul in muls])


def calculate_muls(path: str) -> int:
    sum = 0
    with open(path, "r") as f:
        for line in f:
            sum += calculate_muls_per_line(line)

    return sum


def calculate_muls_with_instructions_per_line(line: str) -> int:
    global do
    instructions = re.finditer(mul_with_instructions_pattern, line)
    sum = 0
    for instruction in instructions:
        ins = instruction.group()
        match ins:
            case "don't()":
                do = False
            case "do()":
                do = True
            case _:
                if do:
                    group = instruction.groups()
                    sum += int(group[0]) * int(group[1])

    return sum


def calculate_muls_with_instructions(path: str) -> int:
    sum = 0
    with open(path, "r") as f:
        for line in f:
            sum += calculate_muls_with_instructions_per_line(line)

    return sum


def main():
    print("Part 1: ", calculate_muls("./3_input.txt"))
    print("Part 2: ", calculate_muls_with_instructions("./3_input.txt"))


main()
