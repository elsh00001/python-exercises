from hashlib import sha1

import requests


def requests_files(nonce: int) -> str:
    # start new session
    sess = requests.Session()
    response = sess.get("https://python.cysec1.de/challenges/upload_file").json()
    # extract data and calculate hash
    joined_list = "".join(sorted(response["unsorted_lists"]))
    file_hash = sha1(joined_list.encode()).hexdigest()
    # post response and return hmac
    response = sess.post("https://python.cysec1.de/challenges/upload_file",
                         data={"nonce": nonce}, files={"file_upload": (response["target_filename"], file_hash)})
    return response.json()["hmac"]