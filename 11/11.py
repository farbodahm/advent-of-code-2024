def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.readline().split()


def count_stones_after_blinks(stones: list[str], num: int) -> int:
    for x in range(num):
        i = 0
        while i < len(stones):
            stone = stones[i]
            if stone == "0":
                stones[i] = "1"
            elif len(stone) % 2 == 0:
                stones.insert(i, stone[: len(stone) // 2])
                right_part = stone[len(stone) // 2 :]
                for j in right_part[: len(right_part) - 1]:
                    if j == "0":
                        right_part = right_part[1:]
                    else:
                        break
                stones[i + 1] = right_part
                i += 1
            else:
                stones[i] = str(int(stone) * 2024)

            i += 1
        print(x)

    return len(stones)


TOTAl_BLINK = 0
cache: dict[tuple[str, int], int] = {}


def count_recursive(stone: str, blink_itr: int) -> int:
    if blink_itr == TOTAl_BLINK:
        return 1

    if (stone, blink_itr) in cache:
        return cache[(stone, blink_itr)]

    if stone == "0":
        cache[(stone, blink_itr)] = count_recursive("1", blink_itr + 1)
        return cache[(stone, blink_itr)]
    elif len(stone) % 2 == 0:
        left_part = stone[: len(stone) // 2]
        right_part = stone[len(stone) // 2 :]
        for j in right_part[: len(right_part) - 1]:
            if j == "0":
                right_part = right_part[1:]
            else:
                break
        cache[(stone, blink_itr)] = count_recursive(
            left_part, blink_itr + 1
        ) + count_recursive(right_part, blink_itr + 1)
        return cache[(stone, blink_itr)]

    cache[(stone, blink_itr)] = count_recursive(str(int(stone) * 2024), blink_itr + 1)
    return cache[(stone, blink_itr)]


def count_stones_after_blinks_part_2(stones: list[str], num: int) -> int:
    global TOTAl_BLINK
    TOTAl_BLINK = num
    total = 0

    for stone in stones:
        total += count_recursive(stone, 0)

    return total


def main():
    stones = parse_input("./11_input.txt")
    print(stones)
    # print(count_stones_after_blinks(stones, 30))
    print(count_stones_after_blinks_part_2(stones, 75))


main()
