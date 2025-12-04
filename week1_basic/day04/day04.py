import requests
from lxml import etree
from urllib.parse import urljoin
import re
import os

BASE = "https://requests.readthedocs.io/en/latest/"

def safe_filename(title):
    return re.sub(r'[\/\\\:\*\?\"\<\>\|]', '_', title).strip() + ".txt"

def crawl_page(url):
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding

    html = etree.HTML(resp.text)

    # 1. 主标题
    title_list = html.xpath("//h1/text()")
    if not title_list:
        print("❌ 未找到 h1，跳过", url)
        return
    title = title_list[0].strip()

    # 2. 正文段落
    paragraphs = html.xpath("//section//p/text()")
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    content = "\n\n".join(paragraphs)

    # 3. 保存本地文件
    txt_dir = os.path.join(os.path.dirname(__file__), "txt")
    os.makedirs(txt_dir, exist_ok=True)
    filename = os.path.join(txt_dir, safe_filename(title))

    with open(filename, "w", encoding="utf-8") as f:
        f.write(title + "\n\n")
        f.write(content)

    print(f"✔ 已保存：{filename}")

def crawl_index():
    resp = requests.get(BASE)
    resp.encoding = resp.apparent_encoding

    html = etree.HTML(resp.text)

    # 1. 获取目录链接（一级目录）
    hrefs = html.xpath("//li[contains(@class,'toctree-l1')]//a/@href")

    for href in hrefs:
        url = urljoin(BASE, href)
        print("➡ 正在爬取：", url)
        crawl_page(url)

crawl_index()

"------------------------------------"
'''
<div class="product-detail">
    <div class="header">
        <h1 class="title">超薄吸顶灯</h1>
        <div class="price-box">
            <span class="label">价格</span>
            <span class="price-value">$129.00</span>
            <span class="discount">限时优惠</span>
        </div>
    </div>

    <div class="specs">
        <h2>规格参数</h2>
        <table>
            <tr><th>尺寸</th><td>30cm</td></tr>
            <tr><th>功率</th><td>18W</td></tr>
            <tr><th>光色</th><td>6000K</td></tr>
        </table>
    </div>

    <div class="reviews">
        <h2>用户评论</h2>

        <div class="review-item">
            <span class="user">Alice</span>
            <p class="content">非常明亮，而且非常薄！</p>
        </div>

        <div class="review-item">
            <span class="user">Bob</span>
            <p class="content">安装方便，性价比高。</p>
        </div>
    </div>
</div>

//div[contains(@class, 'price-box')]//span[contains(@class, 'price-value')]/text()
//div[contains(@class, 'product-detail')]//h1[contains(@class, 'title')]/text()
//div[contains(@class, 'specs')]//table//tr/td/text()
//div[contains(@class, 'specs')]//table//th[contains(text(),'功率')]/following-sibling::td[1]/text()
'''
