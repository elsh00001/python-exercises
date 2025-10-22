import requests


def requests_get(nonce: str) -> str:
    # TODO: implement
    return requests.get("https://executer.python-course.de/challenges/signer", params={"nonce": nonce}).json()['hmac']
    pass
