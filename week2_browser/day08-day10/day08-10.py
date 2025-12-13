import os
import time
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

COOKIE_FILE = "amazon_cookies.json"


# =========================
# cookie 工具函数
# =========================
def save_cookies(cookies, filepath=COOKIE_FILE):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(cookies, f, ensure_ascii=False, indent=2)


def load_cookies(filepath=COOKIE_FILE):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def inject_cookies_to_session(session, cookies):
    for c in cookies:
        session.cookies.set(
            name=c["name"],
            value=c["value"],
            domain=c.get("domain"),
            path=c.get("path", "/")
        )


# =========================
# Selenium 仅用于首次获取 cookies
# =========================
def get_cookies_by_selenium():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(os.path.dirname(BASE_DIR))

    PROFILE_DIR = os.path.join(PROJECT_ROOT, "chrome_profiles", "amazon_profile")
    os.makedirs(PROFILE_DIR, exist_ok=True)

    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_argument("--start-maximized")

    CHROMEDRIVER_PATH = os.path.join(PROJECT_ROOT, "chromedriver.exe")
    service = Service(CHROMEDRIVER_PATH)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.amazon.com")
    time.sleep(5)  # 确保 cookies 写入

    cookies = driver.get_cookies()
    driver.quit()

    save_cookies(cookies)
    return cookies


# =========================
# 获取 session（核心入口）
# =========================
def build_session():
    cookies = load_cookies()
    if cookies is None:
        print("No local cookies found, launching Selenium...")
        cookies = get_cookies_by_selenium()
    else:
        print("Loaded cookies from local file")

    session = requests.Session()
    inject_cookies_to_session(session, cookies)

    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/143.0.0.0 Safari/537.36"
        )
    })
    return session



# =========================
# 解析 HTML 中的评论
# =========================
def parse_reviews(html: str):
    soup = BeautifulSoup(html, "html.parser")
    reviews = []

    for li in soup.select("li[data-hook='review']"):
        title = li.select_one("[data-hook='review-title']")
        body = li.select_one("[data-hook='review-body']")
        rating = li.select_one(
            "[data-hook='review-star-rating'], [data-hook='cmps-review-star-rating']"
        )

        reviews.append({
            "review_id": li.get("id", ""),
            "title": title.get_text(strip=True) if title else "",
            "body": body.get_text(strip=True) if body else "",
            "rating": rating.get_text(strip=True) if rating else "",
        })

    return reviews


# =========================
# 第 1 页：HTML 页面
# =========================
def fetch_first_page(session, asin):
    url = (
        f"https://www.amazon.com/product-reviews/{asin}"
        "?reviewerType=all_reviews&pageNumber=1"
    )
    resp = session.get(url)
    resp.raise_for_status()
    return parse_reviews(resp.text)


# =========================
# 第 2 页起：AJAX GET（&&& 指令流）
# =========================
def fetch_ajax_page(session, asin, page_number):
    url = (
        "https://www.amazon.com/"
        "portal/customer-reviews/ajax/reviews/get/"
        "ref=cm_cr_getr_d_paging_btm_prev_3"
    )

    params = {
        "asin": asin,
        "pageNumber": str(page_number),
        "reviewerType": "all_reviews",
        "sortBy": "",
        "pageSize": "10",
        "filterByStar": "",
        "filterByAge": "",
        "filterByLanguage": "",
        "filterByKeyword": "",
        "shouldAppend": "undefined",
        "deviceType": "desktop",
        "canShowIntHeader": "undefined",
        "reftag": f"cm_cr_getr_d_paging_btm_next_{page_number}",
        "scope": "reviewsAjax0",
    }

    resp = session.get(url, params=params)
    resp.raise_for_status()

    html_segments = []

    # Amazon 返回的是 &&&["append", "#cm_cr-review_list", "<li>...</li>"]
    for block in resp.text.split("&&&"):
        block = block.strip()
        if not block.startswith("["):
            continue
        try:
            arr = json.loads(block)
            if (
                isinstance(arr, list)
                and len(arr) >= 3
                and arr[0] == "append"
                and arr[1] == "#cm_cr-review_list"
            ):
                html_segments.append(arr[2])
        except Exception:
            continue

    if not html_segments:
        return []

    full_html = "".join(html_segments)
    return parse_reviews(full_html)


# =========================
# 主流程
# =========================
def fetch_reviews():
    session = build_session()

    asin = "B0BDF8CVBN"
    all_reviews = []
    # 第 1 页
    page1 = fetch_first_page(session, asin)
    print(f"Page 1: {len(page1)} reviews")
    all_reviews.extend(page1)

    # 第 2~N 页
    for page in range(2, 6):
        reviews = fetch_ajax_page(session, asin, page)
        print(f"Page {page}: {len(reviews)} reviews")
        if not reviews:
            break
        all_reviews.extend(reviews)

    print(f"\nTotal reviews: {len(all_reviews)}")
    if all_reviews:
        print("\nSample review:")
        print(all_reviews[0])


if __name__ == "__main__":
    fetch_reviews()
