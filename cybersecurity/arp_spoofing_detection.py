def detect_arp_spoofing(table: list[str]) -> set[str]:
    internal_table = {}
    suspicious_ips = set()
    for e in table:
        ip = e.split(" ")[0]
        mac = ":".join(o if len(o) == 2 else "0" + o for o in e.split(" ")[-1].split(":"))

        if ip in internal_table:
            if internal_table[ip] != mac:
                suspicious_ips.add(ip)

        else:
            internal_table[ip] = mac

    return suspicious_ips
    pass
