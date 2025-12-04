import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import os

BASE = "https://requests.readthedocs.io/en/latest/"

def safe_filename(title):
    return re.sub(r'[\/\\\:\*\?\"\<\>\|]', '_', title).strip() + ".txt"

def crawl_page(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text)

    # 1. 主标题
    h1 = soup.select_one("h1")
    if not h1:
        print("❌ 未找到 h1，跳过", url)
        return
    title = h1.text.strip()

    # 2. 正文内容
    paragraphs = [p.text.strip() for p in soup.select("section p")]
    content = "\n\n".join(paragraphs)

    # 3. 文件名生成
    txt_dir = os.path.join(os.path.dirname(__file__), "txt")
    os.makedirs(txt_dir, exist_ok=True)
    filename = os.path.join(txt_dir, safe_filename(title))

    # 4. 保存文件
    with open(filename, "w", encoding="utf-8") as f:
        f.write(title + "\n\n")
        f.write(content)

    print("✔ 已保存：", filename)


def crawl_index():
    # 1. 获取目录页
    resp = requests.get(BASE)
    soup = BeautifulSoup(resp.text)

    # 2. 提取一级目录链接
    links = soup.select(".toctree-l1 a")
    for a in links:
        href = a["href"]
        url = urljoin(BASE, href)
        print("➡ 正在爬取：", url)
        crawl_page(url)


crawl_index()
