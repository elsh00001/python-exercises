def rec_factorial(x: int) -> int:
    if x <= 1:
        return 1
    else:
        return x * rec_factorial(x - 1)

def main() -> None:
    # Tests only for student side debugging
    assert rec_factorial(2) == 2
    assert rec_factorial(5) == 120


if __name__ == '__main__':
    main()
