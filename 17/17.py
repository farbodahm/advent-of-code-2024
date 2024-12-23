import re


A: int
B: int
C: int


def parse_input(path: str) -> tuple[int, int, int, list[int]]:
    pattern = r"A: (\d+)\n.*B: (\d+)\n.*C: (\d+)\n\nProgram: (.*)"
    with open(path) as f:
        lines = f.readlines()
    inp: str = "".join(lines)

    regex = re.compile(pattern)
    groups = regex.findall(inp)[0]

    program: list[int] = []
    for p in groups[3]:
        if p == ",":
            continue
        program.append(int(p))

    return (int(groups[0]), int(groups[1]), int(groups[2]), program)


def get_combo_operand(operand: int) -> int:
    if 0 <= operand <= 3:
        return operand

    if operand == 4:
        return A

    if operand == 5:
        return B

    if operand == 6:
        return C

    return -1


def get_program_output(program: list[int]) -> str:
    global A, B, C
    pc = 0
    result: list[str] = []

    while pc < len(program):
        opcode = program[pc]
        operand = program[pc + 1]

        match opcode:
            case 0:
                A = A // (2 ** get_combo_operand(operand))
            case 1:
                B = B ^ operand
            case 2:
                B = get_combo_operand(operand) % 8
            case 3:
                if A == 0:
                    pc += 2
                else:
                    pc = operand
                continue
            case 4:
                B = B ^ C
            case 5:
                result.append(str(get_combo_operand(operand) % 8))
            case 6:
                B = A // (2 ** get_combo_operand(operand))
            case 7:
                C = A // (2 ** get_combo_operand(operand))
            case _:
                raise Exception(f"Unknown Opcode={opcode}")

        pc += 2

    return ",".join(result)


def main():
    global A
    global B
    global C
    A, B, C, program = parse_input("./17_input.txt")
    print(A, B, C, program)

    print("Part 1: ", get_program_output(program))


main()
