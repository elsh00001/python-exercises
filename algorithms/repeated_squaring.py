def fast_power(base: int, exponent: int, modulus: int) -> int:
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        res = fast_power(base, exponent // 2, modulus)
        return (res * res) % modulus
    else:
        res = fast_power(base, (exponent - 1) // 2, modulus)
        return (res * res) * base % modulus
    pass
def main() -> None:
    assert fast_power(3, 16, 49) == 25
    assert fast_power(586561983649063, 982471150907619, 700106762604573) == 482959092846448


if __name__ == "__main__":
    main()
