def read_input(path: str) -> str:
    with open(path) as f:
        return f.readline()


def generate_blocks_string(disk_map: str) -> list[str]:
    counter = 0
    result = []
    is_free_space = False

    for i in disk_map:
        if is_free_space:
            block = ["."] * int(i)
        else:
            block = [str(counter)] * int(i)
            counter += 1

        result += block
        is_free_space = not (is_free_space)

    return result


def free_up_space(blocks: list[str]) -> list[str]:
    i, j = 0, len(blocks) - 1

    while i < j:
        while blocks[i] != "." and i < len(blocks) and i < j:
            i += 1
        while blocks[j] == "." and j > 0 and j > i:
            j -= 1

        blocks[i] = blocks[j]
        blocks[j] = "."

    return blocks


def calculate_checksum(blocks: list[str]) -> int:
    total = 0

    for i, j in enumerate(blocks):
        if j == ".":
            break
        total += i * int(j)

    return total


def main():
    inp = read_input("./9_input.txt")
    blocks_str = generate_blocks_string(inp)
    blocks_optimized = free_up_space(blocks_str)
    print(calculate_checksum(blocks_optimized))


main()
