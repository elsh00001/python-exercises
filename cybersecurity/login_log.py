import json
from collections import defaultdict


def login_log(log: str) -> dict[str, list[str]]:
    json_log = json.loads(log)
    read_dict = defaultdict(list)
    for attempt in json_log:
        if not attempt["success"]:
            read_dict[attempt["username"]].append(attempt["ip"])
    return {
        user: sorted(read_dict[user]) for user in read_dict if len(read_dict[user]) >= 5
    }
