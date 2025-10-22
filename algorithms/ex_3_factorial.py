def factorial(n: int) -> int:
    # TODO implement
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
    pass


def main() -> None:
    assert factorial(3) == 6
    assert factorial(9) == 362880
    assert factorial(42) == 1405006117752879898543142606244511569936384000000000


if __name__ == '__main__':
    main()
