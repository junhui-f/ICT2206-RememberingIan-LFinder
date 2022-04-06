import requests

def capture_baseline(URL, HEADERS, COOKIES):
    PATH = URL
    res = requests.post(url=PATH, headers=HEADERS, cookies=COOKIES)
    return str(res.text)