def elgamal_decrypt(private_key: tuple[int, int, int], message: tuple[int, int]) -> int:
    p = private_key[0]
    x = private_key[2]
    c1 = message[0]
    c2 = message[1]
    s = pow(c1, x, p)
    sinverse = pow(s, -1, p)
    m = (c2 * sinverse) % p
    return m