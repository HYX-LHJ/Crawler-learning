import requests


url = "https://api.juejin.cn/search_api/v1/search"

params = {
    "aid": "2608",
    "uuid": "7551251884074829366",
    "spider": "0",
    "query": "mysql",
    "id_type": "0",
    "cursor": "0",
    "limit": "20",
    "search_type": "0",
    "sort_type": "0",
    "version": "1"
}



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

resp = requests.get(url, headers=headers, params=params)
print(resp.status_code)

print(resp.json())
