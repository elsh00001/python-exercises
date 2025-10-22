def reverse_words(s: str) -> str:
    # TODO implement
    split_words = s.split()
    split_words.reverse()
    return ' '.join(split_words)
    pass


def main() -> None:
    assert reverse_words("World! Hello") == "Hello World!"
    assert reverse_words("This is a test") == "test a is This"
    assert reverse_words("Cysec ") == " Cysec"


if __name__ == '__main__':
    main()
