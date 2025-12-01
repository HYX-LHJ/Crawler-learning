📘 Python 爬虫学习路线（12 月 · 工作日 1–1.5 小时）

目标：
在 12 月达到“能独立爬常见网站 + 能逆向加密接口”的工程化能力。

本路线共 4 周，遵循从基础 → 浏览器模拟 → JS 逆向 → 反爬与项目化的渐进式设计。
所有任务时间适配 上班族每日 1–1.5 小时 的学习节奏。

🎯 最终掌握能力（12 月结束）

能爬取常见静态网站与常规结构化内容

熟练使用 Playwright/Selenium 处理动态加载

能抓包分析接口、定位数据源

能逆向 JS 加密参数（sign/token/timestamp）

能将加密逻辑迁移到 Python

能绕过常见反爬策略（User-Agent、Cookie、Headers、限频）

能搭建可复用、可维护的爬虫工程结构

能把 request + browser 结合起来做复杂项目

🗓 学习计划（按周拆解）
Week 1 · 核心基础：HTTP + HTML 解析 + requests

目标：理解浏览器与服务器的本质交互关系，并掌握基础爬虫三件套。

学习重点：

HTTP（方法、状态码、Headers、Cookie/Session）

浏览器与服务器的通信流程

requests 基础与 session 维持

HTML + DOM 结构

CSS Selector & XPath（必须精通）

解析库：BeautifulSoup / lxml

每日安排：

Day 1：HTTP 原理、Headers、Cookie

Day 2：requests 的请求方式、参数与 Session

Day 3：CSS Selector 解析

Day 4：XPath 实战

Day 5：综合练习：

豆瓣 Top250

知乎热榜

简单新闻站

✔ 熟练执行以上内容后，你已能轻松应对绝大多数静态网站。

Week 2 · 动态网站与浏览器模拟：Playwright/Selenium + 抓包

目标：掌握“真实浏览器级别”的网页处理能力，解决 JS 渲染与动态加载。

学习重点：

Playwright（推荐）或 Selenium

自动化登录、点击、滚动加载

抓包：Chrome DevTools → Network → XHR

将浏览器 Cookie 复用到 requests

渲染型页面如何找到真实数据接口

每日安排：

Day 6：安装 Playwright，运行第一个脚本

Day 7：自动化操作（输入、点击、滑动）

Day 8：抓包找数据接口（XHR / fetch / websocket）

Day 9：Cookie 复制给 requests，完成半自动登录

Day 10：实战项目：

爬取一个动态加载的网站完整数据

✔ 完成本周，你的爬虫能穿过大部分“页面渲染”障碍。

Week 3 · JS 逆向与加密接口：sign/token 复现

目标：破解网站的 JS 加密逻辑，能逆向出请求所需的 sign、token、timestamp 参数。

学习重点：

JS 混淆识别（format + 搜关键字）

Chrome 调试（breakpoint / Scope / Callstack）

常见加密算法：

AES（ECB/CBC）

RSA

MD5 / SHA256

HMAC-SHA256

JS → Python 加密函数迁移

hook XHR / fetch / Crypto 获取参数

每日安排：

Day 11：认识与格式化混淆 JS

Day 12：定位加密参数（token、sign）

Day 13：PyCryptodome 复现 AES / HMAC / RSA

Day 14：浏览器断点调试、hook 技术

Day 15：实战逆向：

找到一个真实含 sign/timestamp 的接口

逆向加密方式

Python 成功复现

成功拿到数据

✔ 这是爬虫进阶的分水岭：过了 JS 逆向，你能处理大多数真实业务网站。

Week 4 · 与反爬战斗：指纹、代理池、限频、工程化

目标：掌握应对常见反爬手段的技巧，并构建可复用的爬虫工程结构。

学习重点：

浏览器指纹检测（WebGL、Canvas、User-Agent、Screen）

Cloudflare/Akamai 的常见策略（理解，不要求破解）

限频/Ratelimit 策略

IP 代理轮换

异步爬虫（asyncio + aiohttp）

项目结构化

每日安排：

Day 16：指纹检测、防检测浏览器原理

Day 17：IP 代理池（开源 / 自建）

Day 18：Cloudflare、行为识别、反 bot

Day 19：用 aiohttp 重写一个之前的项目

Day 20：期末项目（任选其一）：

电商网站商品列表完整爬取

登录后才能查看的历史内容爬取

“真实用户行为”模拟抓取（浏览器自动化）

✔ 完成第 4 周，你已经具备工程级爬虫开发能力。

📦 推荐工具与技术栈
🔧 必备 Python 库
requests
beautifulsoup4
lxml
playwright
selenium (optional)
pycryptodome
aiohttp

🔍 必备工具

Chrome DevTools（抓包）

VSCode / PyCharm

mitmproxy（抓 HTTPS 很强）

Fiddler（更直观）

🏗 建议的项目结构（可直接放仓库）
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
