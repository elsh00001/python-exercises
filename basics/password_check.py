def password_check(username: str, password: str) -> str:
    score = 3
    length = len(password)
    if length < 12:
        score -= 1
    if password.isalnum():
        score -= 1
    if username in password or "12345" in password or "qwert" in password or "password" in password:
        score -= 1
    if score == 3:
        return "good"
    if score == 2:
        return "Ok"
    if score == 1:
        return "weak"
    return "bad"
    pass


def main() -> None:
    # Tests only for student side debugging
    assert password_check("Hans", "asdhf2324#fq1sa") == "good"
    assert password_check("Dieter", "securepassword!") == "Ok"
    assert password_check("Kevin", "Kevin2002!") == "weak"
    assert password_check("Bob", "qwertz") == "bad"


if __name__ == '__main__':
    main()
