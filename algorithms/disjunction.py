def disjunction(set1: set, set2: set) -> bool:
    for i in set1:
        if i in set2:
            return False
    return True
    pass


def main() -> None:
    # Tests for student side debugging only
    assert not disjunction({1, 2, 3}, {2, 5})
    assert disjunction({"Pizza"}, {"Pineapple", "Cucumbers", "lettuce"})


if __name__ == '__main__':
    main()
