def solution(n, l, r):
    return count_1(r) - count_1(l-1)


def count_1(idx):
    if idx <= 5:
        return '11011'[:idx].count('1')

    power = 1
    while 5 ** (power + 1) <= idx:
        power += 1

    base = 5 ** power
    section, remainder = divmod(idx, base)
    if section == 1:
        return section * (4 ** power) + count_1(remainder)
    elif section == 2:
        return section * (4 ** power)
    else:
        return (section - 1) * (4 ** power) + count_1(remainder)


if __name__ == "__main__":
    n = 3
    l = 4
    r = 17
    print(solution(n, l, r))
