def generate_keys(p: int, g: int, x: int):
    if not is_prime(p):
        raise ValueError("Invalid prime!")

    reference = set(i for i in range(1, p))
    if set((g**i) % p for i in range(1, p)) != reference:
        raise ValueError("Invalid generator!")

    h = pow(g, x, p)
    return (p, g, x), (p, g, h)


def is_prime(n):
    for c in range(2, int(n**0.5 + 1)):
        if n % c == 0:
            return False
    return n > 1
