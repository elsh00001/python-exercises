def slaac_reversion(ipv6_address: str) -> str:
    segments = ipv6_address.split(":")
    bits_to_alter = segments[4][:2]
    flipped_bit = "{:02x}".format(int(bits_to_alter, 16) ^ 2)
    mac_address = f"{flipped_bit}:{segments[4][2:]}:{segments[5][:2]}:{segments[6][2:]}:{segments[7][:2]}:{segments[7][2:]}"
    return mac_address.upper()
    pass


if __name__ == '__main__':
    assert slaac_reversion('3cd7:23d1:2846:3c2d:4cbb:90ff:fecb:1c9f') == '4E:BB:90:CB:1C:9F'
