# Python 爬虫学习路线（12 月 · 工作日 1–1.5 小时）

## 目标

在 12 月达到能够 **爬取常见网站 + 逆向加密接口** 的工程能力。

本路线分为 4 周，从基础 → 动态渲染 → JS 逆向 → 反爬与工程化，完全适配上班族每天 1–1.5 小时的节奏。

---

## 最终掌握能力

- 熟练爬取常见静态网页内容
- 熟悉 Playwright/Selenium，能处理动态加载页面
- 能抓包找到真实数据接口
- 能逆向 JS 加密参数（sign/token/timestamp）
- 能将加密算法迁移到 Python（AES/HMAC/RSA）
- 能处理登录、Cookie 维持与反爬
- 能构建可维护的爬虫项目结构
- 能结合 requests + 浏览器模拟完成复杂抓取

---

## 学习计划（按周拆解）

### Week 1 · 基础掌握：HTTP、HTML、requests

**学习重点：**

- HTTP 基础（方法、状态码、Headers、Cookie、Session）
- requests 的基本使用与 Session 机制
- HTML DOM 结构解析
- CSS Selector 与 XPath
- BeautifulSoup / lxml 基礎使用

**每日安排：**

| Day   | 内容 |
|-------|------|
| Day 1 | HTTP 原理、Headers 与 Cookie |
| Day 2 | requests 基础（参数、Header、Session） |
| Day 3 | CSS Selector 实战解析 |
| Day 4 | XPath 解析练习 |
| Day 5 | 练习项目：<br>• 豆瓣 Top250<br>• 知乎热榜<br>• 任意新闻站 |

---

### Week 2 · 动态网页与浏览器模拟：Playwright / Selenium

**学习重点：**

- Playwright（推荐）或 Selenium
- 自动化登录、点击、输入、滚动加载
- Chrome DevTools 抓包（Network → XHR）
- 从动态页面定位真实数据接口
- 浏览器 Cookie 提取并交给 requests 使用

**每日安排：**

| Day   | 内容 |
|-------|------|
| Day 6 | 环境安装，与第一个自动化脚本 |
| Day 7 | 页面操作（输入、点击、滑动、等待元素） |
| Day 8 | 抓包查找接口（XHR / fetch） |
| Day 9 | 浏览器登录 → 导出 Cookie → 用 requests 复用 |
| Day 10 | 实战：爬一个完全动态加载的网站 |

---

### Week 3 · JS 逆向与加密接口复现

**学习重点：**

- 格式化与分析混淆 JS（Source Map、关键字搜索）
- Chrome DevTools 断点调试（Scope/Call Stack）
- 常见加密：
  - AES（ECB/CBC）
  - HMAC-SHA256
  - RSA
  - MD5 / SHA256
- 加密函数迁移（JS → Python）
- hook fetch/XHR/Crypto 获取中间参数

**每日安排：**

| Day   | 内容 |
|-------|------|
| Day 11 | 混淆 JS 格式化、查找加密函数 |
| Day 12 | 分析 sign/token/timestamp 的生成逻辑 |
| Day 13 | 用 PyCryptodome 复现 AES/HMAC/RSA |
| Day 14 | 浏览器断点调试、hook 工具 |
| Day 15 | 实战逆向一个真实含 sign/timestamp 的接口 |

---

### Week 4 · 反爬策略与工程化

**学习重点：**

- 浏览器指纹（User-Agent、Canvas/WebGL、屏幕参数）
- Cloudflare / Akamai 的常见反爬策略
- 限频机制与重试策略
- 代理池（免费/付费、自建）
- 异步爬虫（aiohttp + asyncio）
- 项目结构化拆分

**每日安排：**

| Day   | 内容 |
|-------|------|
| Day 16 | 反爬与指纹检测机制 |
| Day 17 | 构建代理池并实现自动轮换 |
| Day 18 | 常见反爬策略理解与应对 |
| Day 19 | 用 aiohttp 重写爬虫 |
| Day 20 | 期末项目（任选其一）：<br>• 电商站点完整商品抓取<br>• 登录后可见数据爬取<br>• 自动化浏览器模拟真实用户行为 |

---

## 推荐工具与技术栈

### 必备 Python 库

- requests
- beautifulsoup4
- lxml
- playwright
- selenium
- pycryptodome
- aiohttp

### 必备工具

- Chrome DevTools（抓包）
- Fiddler or mitmproxy（HTTPS 抓包）
- VSCode / PyCharm

---

## 项目结构建议（可直接用于你的 GitHub 仓库）

```
spider-learning/
│
├── week1_basic/
├── week2_browser/
├── week3_reverse/
├── week4_antibot/
│
├── examples/
├── tools/
│   ├── crypto_utils.py
│   ├── proxy_manager.py
│   └── browser_cookie.py
│
└── README.md
```
