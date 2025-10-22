def replacement_cipher(key_dict: dict[str, str], cipher_text: str) -> str:
    decipher = ""
    for cipher in cipher_text:
        if cipher in key_dict:
            decipher += key_dict[cipher]
        else:
            decipher += cipher
    return decipher
    pass


def main() -> None:
    # Tests for student side debugging only
    assert replacement_cipher({"e": "c", "g": "a", "d": "f", "v": "e", "r": "b"}, "egdv rgrv") == "cafe babe"


if __name__ == '__main__':
    main()
