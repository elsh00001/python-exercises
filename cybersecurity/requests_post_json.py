import requests


def requests_post_json(nonce: str) -> str:
    # TODO: implement
    sess = requests.Session()
    data = sess.get("https://python.cysec1.de/challenges/json_post").json()
    # extract needed data
    captcha = data["captcha"]
    function_name = data["requested_function"]
    captcha_result = eval(f"str.{function_name}('{captcha}')")
    # post result
    response = sess.post("https://python.cysec1.de/challenges/json_post",
                         json={'solution': captcha_result, "nonce": nonce})
    return response.json()["hmac"]
    pass
