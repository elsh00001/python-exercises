def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def is_prime(n: int) -> int:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def compute_d(p: int, q: int, e: int) -> int:
    phi = (p - 1) * (q - 1)
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p and q need to be prime")

    if gcd(e, phi) != 1:
        raise ValueError("e and phi(N) need to be coprime.")

    d = pow(e, -1, phi)
    return d