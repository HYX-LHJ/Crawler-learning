import requests

from day03 import load_cookie_str,open_browser

def main():
    open_browser()
    cookie_str = load_cookie_str()
    headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": cookie_str
}

    url = "https://api.juejin.cn/interact_api/v1/message/count"
    params = {
    "aid": 2608,
    "uuid": "7551251884074829366",
    "spider": 0
}

    resp = requests.get(url, headers=headers, params=params)
    print(resp.json())

if __name__ == '__main__':
    main()

