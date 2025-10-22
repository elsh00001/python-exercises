def fahrenheit_to_celsius(f):
    # remember to round to two decimal digits
    return round((5 / 9) * (f - 32), 2)
    pass


def main() -> None:
    assert fahrenheit_to_celsius(98) == 36.67
    assert fahrenheit_to_celsius(-35) == -37.22
    assert fahrenheit_to_celsius(1337) == 725.0


if __name__ == '__main__':
    main()
