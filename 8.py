from collections import defaultdict


def parse_input(path: str) -> dict[str, list[tuple[int, int]]]:
    result: dict[str, list[tuple[int, int]]] = defaultdict(list[tuple[int, int]])

    with open(path) as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line):
                if char != "." and char != "\n":
                    result[char].append((i, j))

    return result


def get_map_length(path: str) -> tuple[int, int]:
    with open(path) as f:
        mat = f.readlines()
    return (len(mat), len(mat[0]))


def count_anti_nodes(
    antennas: dict[str, list[tuple[int, int]]], mat_len: tuple[int, int]
) -> int:
    anti_nodes: set[tuple[int, int]] = set()

    for antenna in antennas.values():
        for i in range(len(antenna)):
            for j in range(i + 1, len(antenna)):
                diff_x = abs(antenna[i][0] - antenna[j][0])
                diff_y = abs(antenna[i][1] - antenna[j][1])

                possible_anti_nodes: list[tuple[int, int]] = []
                if antenna[i][0] < antenna[j][0]:
                    if antenna[i][1] < antenna[j][1]:
                        possible_anti_nodes.append(
                            (antenna[i][0] - diff_x, antenna[i][1] - diff_y)
                        )
                        possible_anti_nodes.append(
                            (antenna[j][0] + diff_x, antenna[j][1] + diff_y)
                        )
                    else:
                        possible_anti_nodes.append(
                            (antenna[i][0] - diff_x, antenna[i][1] + diff_y)
                        )
                        possible_anti_nodes.append(
                            (antenna[j][0] + diff_x, antenna[j][1] - diff_y)
                        )
                else:
                    if antenna[i][1] < antenna[j][1]:
                        possible_anti_nodes.append(
                            (antenna[i][0] + diff_x, antenna[i][1] - diff_y)
                        )
                        possible_anti_nodes.append(
                            (antenna[j][0] - diff_x, antenna[j][1] + diff_y)
                        )
                    else:
                        possible_anti_nodes.append(
                            (antenna[i][0] + diff_x, antenna[i][1] + diff_y)
                        )
                        possible_anti_nodes.append(
                            (antenna[j][0] - diff_x, antenna[j][1] - diff_y)
                        )

                for anti_node in possible_anti_nodes:
                    if (
                        0 <= anti_node[0] < mat_len[0]
                        and 0 <= anti_node[1] < mat_len[1]
                    ):
                        anti_nodes.add(anti_node)

    return len(anti_nodes)


def main():
    antennas = parse_input("./8_input.txt")
    mat_len = get_map_length("./8_input.txt")

    print("Part 1: ", count_anti_nodes(antennas, mat_len))


main()
