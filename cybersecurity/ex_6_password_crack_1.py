from hashlib import md5

def crack_password(correct_hash: str, wordlist: str) -> str:
    # TODO: implement
    with open(wordlist) as file:
        for line in file:
            password = line.strip()
            hashed_password = md5(password.encode()).hexdigest()
            if correct_hash == hashed_password:
                return password

    return ""

    pass
