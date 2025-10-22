def gcd_output(x: int, y: int) -> list[str]:
    new_list = []
    while y != 0:
        factor = x // y
        rest = x % y
        new_list.append(f"{x} = {factor} * {y} + {rest}")

        # swap like euclid
        x = y
        y = rest
        if rest == 1:
            break
    return new_list

    pass

if __name__ == '__main__':
    assert gcd_output(11, 7) == ['11 = 1 * 7 + 4', '7 = 1 * 4 + 3', '4 = 1 * 3 + 1', '3 = 3 * 1 + 0']
