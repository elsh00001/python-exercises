def simple_hash(txt: str) -> str:
    # TODO: implement
    # remember that the '0x' part is not considered part of the hex-number
    counter = 42
    number = 1
    for i in txt:
        counter += ord(i) * number
        number += 1
    counter = counter ** 2
    hexformat = hex(counter)[2:].rstrip("0")

    while len(hexformat) < 128:
        counter = counter ** 2
        hexformat = hex(counter)[2:].rstrip("0")

    return hexformat[-64:].rstrip("0")
    pass
