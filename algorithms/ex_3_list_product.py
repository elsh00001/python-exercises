# Write a function called list_product, which takes a list of integers and returns their product. You have to use a for loop to do this!

def list_product(lst: list) -> int:
    # TODO implement
    res = 1
    if not lst:
        return 0
    else:
        for i in lst:
            res *= i
    return res
    pass


def main() -> None:
    assert list_product([1, 4, 7, 2]) == 56
    assert list_product([3, -8, -9, 12]) == 2592
    assert list_product([]) == 0

if __name__ == '__main__':
    main()
