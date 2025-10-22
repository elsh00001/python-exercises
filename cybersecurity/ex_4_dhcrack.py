def crack_dh_exchange(p: int, g: int, A: int, B: int) -> int:
    # TODO implement
    a = 0
    for i in range(1, p):
        if A == pow(g, i, p):
            a = i
    return pow(B, a, p)
    pass


def main() -> None:
    # Tests for student side debugging only
    assert crack_dh_exchange(613, 560, 217, 150) == 285
    assert crack_dh_exchange(941, 101, 335, 500) == 608


if __name__ == '__main__':
    main()
