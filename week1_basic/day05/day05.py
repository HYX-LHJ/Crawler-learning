import requests
from bs4 import BeautifulSoup
import json


url = "https://www.amazon.com/portal/customer-reviews/ajax/reviews/get/ref=cm_cr_getr_d_paging_btm_prev_3"


params = {
    "sortBy": "",
    "reviewerType": "all_reviews",
    "formatType": "",
    "mediaType": "",
    "filterByStar": "",
    "filterByAge": "",
    "pageNumber": "3",
    "filterByLanguage": "",
    "filterByKeyword": "",
    "shouldAppend": "undefined",
    "deviceType": "desktop",
    "canShowIntHeader": "undefined",
    "reftag": "cm_cr_getr_d_paging_btm_prev_3",
    "pageSize": "10",
    "asin": "B0BDF8CVBN",
    "scope": "reviewsAjax3"
}




cookies = {
    "session-id": "136-6617515-9756211",
    "ubid-main": "135-3541121-6672900",
    "skin": "noskin",
    "id_pkel": "n1",
    "id_pk": "eyJuIjoiMSIsImFmIjoiMSIsImNjIjoiMSJ9",
    "at-main": "Atza|gQAcT8UuAwEBAjQcUcaI__5SlWzPBCHyuTj-ElgmSpVOJ4cvY7ZKRdA64rXKwz4B50xchh8uCMiBEUvWZh2EUP_-Z-62OWnMUi1np2BBcnZgrZPwP99RNv9Y3l5SkJtkmVd1p5Q2Mm-mvwcST74wAGx9Z-St8S1Be_aDDSWPNQZ_VpwWA-rLjg77SgQ_MmMeo5BuyqWfoV3fruA4yEetBdzLNBtXy_Qi0ATnDhe2wQ1oROdWnweyPNR_1JilpspW7_Alb7rAU1cPlvtAzOqw9yS4IFuwRnF569RGkTmEmzTN8a0F3uLo_n0_geuYWqqtgDqWEzktOECkNDa5Ok5TWJh1hCOkrGAIMLYt6g",
    "sess-at-main": "uuSUk1tgLQU3YlZdpi0rH5Z/TsvKeCTpyRumnWcVHpE=",
    "session-id-time": "2082787201l",
    "i18n-prefs": "USD",
    "lc-main": "en_US",
    "rxc": "AKq8hXZEA12VPNAff90",
    "csm-hit": "tb:CXJ03H8MDEWC9DPQW8YH+b-0K6T1K33PPXCSDNQ7WE0|1765103140035&t:1765103140035&adb:adblk_yes",
    "session-token": "XVne1RMPh77PIUtjyfFU+2qROpN/yR34KccbI2BUliPVuVSyUL5UH8kL9R2+dP5KepQC0TRkCqObQTLAvC4Zqs0326UVahgzbYJxx8I3hfFQtlmDxsfmCKbDRLB3m6Ib52bIpHC0mjWXrhxBSsNMKVehuJt4zgCDaYNq4cP/us+Rr2ywUq0fB3ynAMOgEWyf9AXC3v4sRFJcpXXtDy1xDzip4h8yM5RrDeysU5l5FLkiztmjXKdxpKBONcDOgwx0uaHBKIGK9g2cTxTjMQ2R4VFU6XiiwPX5QP5X8w93+A9bObhWE27PpmIQPRzoAAn/39IaiZNRXrY9TiVdmZAvslphmr2vV0nXyndyyKoWn1rNspA/jCXkbV++zWdunQYt",
    "x-main": "91KDkRH@aIDfI4B4hP1Ojt9vCI1vfoQv2585lBuWB7p9dAn@MjRdmpfSEWGChtxk"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

# ... existing code ...
# ... existing code ...
# 将单页评论抓取、块解析与结构化封装

def fetch_review_page(asin: str, page: int) -> list:
    params = {
        "sortBy": "",
        "reviewerType": "all_reviews",
        "formatType": "",
        "mediaType": "",
        "filterByStar": "",
        "filterByAge": "",
        "pageNumber": str(page),  # 动态页码
        "filterByLanguage": "",
        "filterByKeyword": "",
        "shouldAppend": "undefined",
        "deviceType": "desktop",
        "canShowIntHeader": "undefined",
        "reftag": f"cm_cr_getr_d_paging_btm_next_{page}",
        "pageSize": "10",
        "asin": asin,             # 动态 ASIN
        "scope": "reviewsAjax0",
    }

    resp = requests.get(url, headers=headers, cookies=cookies, params=params)
    blocks = resp.text.split("&&&")

    html_segments = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        try:
            arr = json.loads(block)
            if len(arr) >= 3 and arr[0] == "append" and arr[1] == "#cm_cr-review_list":
                html_segments.append(arr[2])
        except Exception:
            continue

    full_html = "".join(html_segments)
    soup = BeautifulSoup(full_html, "html.parser")

    reviews = []
    for li in soup.find_all("li", {"data-hook": "review"}):
        try:
            reviews.append({
                "review_id": li.get("id", ""),
                "author": (li.find("span", {"class": "a-profile-name"}) or {}).get_text(strip=True),
                "rating": (li.find("i", {"class": "a-icon-star"}) or {}).get_text(strip=True),
                "title": (li.find("a", {"data-hook": "review-title"}) or {}).get_text(strip=True),
                "date": (li.find("span", {"data-hook": "review-date"}) or {}).get_text(strip=True),
                "content": (li.find("span", {"data-hook": "review-body"}) or {}).get_text(strip=True),
            })
        except Exception:
            continue
    return reviews

# 聚合多页评论

def get_all_reviews(asin: str, max_pages: int = 5) -> list:
    all_reviews = []
    for p in range(1, max_pages + 1):
        page_reviews = fetch_review_page(asin, p)
        # 打印每页实际获取的评论数量
        print(f"第 {p} 页获取 {len(page_reviews)} 条评论")
        # 打印每条评论的简要信息
        for i, r in enumerate(page_reviews, 1):
            print(f"  - [{i}] {r.get('author','')} | {r.get('rating','')} | {r.get('title','')[:50]}")
        all_reviews.extend(page_reviews)
    return all_reviews

# 保存为 JSON 文件（中文不转义，格式化美观）

def save_to_json(data: list, asin: str) -> None:
    filename = f"{asin}_reviews.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 示例调用

if __name__ == "__main__":
    asin = "B0BDF8CVBN"
    reviews = get_all_reviews(asin, max_pages=20)
    save_to_json(reviews, asin)
