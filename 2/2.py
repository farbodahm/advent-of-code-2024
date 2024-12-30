def is_safe(report: list[int]) -> bool:
    is_increasing: bool = (report[1] - report[0]) > 0
    for i in range(1, len(report)):
        if is_increasing:
            if not (0 < (report[i] - report[i - 1]) <= 3):
                return False
        else:
            if not (-3 <= (report[i] - report[i - 1]) < 0):
                return False

    return True


def calculate_safe_reports(path: str) -> int:
    result = 0
    with open(path, "r") as f:
        for report in f:
            levels = list(map(int, report.split()))
            if is_safe(levels):
                result += 1

    return result


def is_safe_with_dampener(report: list[int]) -> bool:
    for i in range(len(report)):
        report_with_dampener = report[:i] + report[i+1:]
        if is_safe(report_with_dampener):
            return True
    return False


def calculate_safe_reports_part_two(path: str) -> int:
    result = 0
    with open(path, "r") as f:
        for report in f:
            levels = list(map(int, report.split()))
            if is_safe_with_dampener(levels):
                result += 1

    return result


def main():
    print("Part 1:", calculate_safe_reports("./2_input.txt"))
    print("Part 2:", calculate_safe_reports_part_two("./2_input.txt"))


main()
