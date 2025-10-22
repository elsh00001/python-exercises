import ipaddress


def find_smallest_cidr(ips: list[str]) -> str:
    ip_ints = [int(ipaddress.IPv4Address(ip)) for ip in ips]
    min_ip = min(ip_ints)
    max_ip = max(ip_ints)
    common_prefix_len = 32 - (max_ip ^ min_ip).bit_length()
    network = ipaddress.IPv4Network((min_ip, common_prefix_len), strict=False)
    return str(network)
    pass


if __name__ == "__main__":
    assert find_smallest_cidr(["192.168.1.1", "192.168.1.2", "192.168.1.5"]) == "192.168.1.0/29"
    assert find_smallest_cidr(["10.0.0.1", "10.0.0.2", "10.0.0.15"]) == "10.0.0.0/28"
    assert find_smallest_cidr(["172.16.1.1", "172.16.1.254"]) == "172.16.1.0/24"
