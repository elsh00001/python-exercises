def zodiac(birth_year: int) -> str:
    # TODO implement
    remainder = birth_year % 12
    zodiac = {0: "Monkey", 1: "Rooster", 2: "Dog", 3: "Pig",
              4: "Rat", 5: "Ox", 6: "Tiger", 7: "Rabbit", 8: "Dragon", 9: "Snake", 10: "Horse", 11: "Goat"
              }

    return zodiac[remainder]
    pass


def main() -> None:
    # Tests for student side debugging only
    assert zodiac(2023) == "Rabbit"
    assert zodiac(2002) == "Horse"


if __name__ == '__main__':
    main()
