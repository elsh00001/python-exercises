# you must not import anything for this task
def verify_iban(iban: str) -> bool:
    numerical = {'a': "10", 'b': "11", 'c': "12", 'd': '13', 'e': '14', 'f': '15', 'g': '16', 'h': '17', 'i': '18',
                 'j': '19', 'k': '20', 'l': '21', 'm': '22', 'n': '23', 'o': '24', 'p': '25', 'q': '26', 'r': '27',
                 's': '28', 't': '29', 'u': '30', 'v': '31', 'w': '32', 'x': '33', 'y': '34', 'z': '35'}
    first = iban[0:4]
    new_iban = iban[4:] + first
    result = ""
    for i in new_iban:
        if i.isalpha():
            result += numerical[i.lower()]
        else:
            result += i
    result = int(result)
    if result % 97 == 1:
        return True
    return False
    pass


def main() -> None:
    assert verify_iban('GB82WEST12345698765432') is True
    assert verify_iban('DE89370400440532013000') is True
    assert verify_iban('GB82WEST12345698765431') is False


if __name__ == "__main__":
    main()
