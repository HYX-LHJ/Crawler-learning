from playwright.sync_api import sync_playwright
import json

def open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://juejin.cn")

        print("请在浏览器中手动登录掘金...")
        page.pause()

        # 重点：抓取 api.juejin.cn 的 Cookie
        cookies = context.cookies(["https://api.juejin.cn"])

        print("\n==== API 域名 Cookie ====\n")
        with open("juejin_cookies.json", "w", encoding="utf-8") as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)
        print("Cookie 已保存到 juejin_cookies.json")


        cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies])
        print("\n==== 可用于 requests 的 cookie_str ====\n")
        print(cookie_str)
        

        browser.close()

def load_cookie_str():
    with open("juejin_cookies.json", "r", encoding="utf-8") as f:
        cookies = json.load(f)
    cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies])
    return cookie_str

if __name__ == "__main__":
    open_browser()
