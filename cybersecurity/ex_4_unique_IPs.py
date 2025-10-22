def unique_IPs(ip_list: list[str]) -> list[str]:
    # TODO implement
    unique = []
    for ip in ip_list:
        if ip not in unique:
            unique.append(ip)
    return unique
    pass


def main() -> None:
    # Tests for student side debugging only
    assert unique_IPs(["47.78.23.151", "211.216.183.149", "47.78.23.151", "116.118.242.134"]) == ["47.78.23.151", "211.216.183.149", "116.118.242.134"]
    assert unique_IPs(['29.66.248.231', '29.66.248.231', '29.66.248.231']) == ['29.66.248.231']


if __name__ == '__main__':
    main()
