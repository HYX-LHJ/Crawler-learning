# 📝 Day02 — requests 基础（参数、Header、Session）学习笔记

## 1. 今日目标

- 掌握 requests 的基础使用方式
- 理解 GET / POST 的区别与抓包判断方法
- 学习如何添加 Header（伪装浏览器）
- 学习 Session 的原理与作用（Cookie 自动保存）
- 完成掘金 cursor-based 分页爬虫
- 理解 Cookie 何时需要、何时不需要
- 能判断一个接口是否需要登录态

## 2. requests 基础

### ✔ 2.1 GET 请求（参数在 URL 上）

```python
requests.get(url, params={"query": "mysql", "cursor": "0"})
```

GET 的 Query 参数会自动追加到 URL 后：

```
?query=mysql&cursor=0
```

### ✔ 2.2 POST 请求（参数在 Body 中）

两种 Body 常见写法：

**Form Data**

```python
requests.post(url, data={"name": "Alex", "pwd": "123"})
```

**JSON Body（最常用）**

```python
requests.post(url, json={"name": "Alex", "pwd": "123"})
```

> 💡 判断 GET / POST 永远以 DevTools → Request Method 为准。

## 3. Headers（伪装浏览器、防反爬的关键）

最常用的 Headers：

```python
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://juejin.cn/",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
```

### 你今天学会的是：

- **User-Agent** → 浏览器身份信息（最重要）
- **Cookie** → 登录状态/权限验证
- **Authorization** → Token 鉴权
- **Accept-Language** → 网站语言偏好

### 判断接口是否需要 Cookie：

看 Method、Response、Set-Cookie、隐身模式访问。

## 4. Session（今天最重要的概念）

### ✔ 4.1 Session 是什么？

```python
s = requests.Session()
```

### Session 的两个核心能力：

#### ① 自动保存 Cookie

例如：

```python
s.get("https://site.com/login")      # 服务器下发 Set-Cookie
s.get("https://site.com/profile")   # 自动携带 Cookie
```

这就模拟了"浏览器的一次会话"。

#### ② 复用连接，提高性能

Session 会复用 TCP/TLS 连接，比单独 requests 更快、更像浏览器。

### ✔ 4.2 查看 Session 中的 Cookie

```python
s.cookies.get_dict()
```

如果是：

```python
{}
```

说明该接口 "不需要登录 Cookie"。

如果不为空，则说明 Session 记录了服务器返回的身份信息。

## 5. 今天的深度理解

### ✔ 哪些接口需要 Cookie？哪些不需要？

### 你已经具备以下判断能力：

**1）看响应是否有 Set-Cookie**
- 有 → 很可能需要
- 无 → 多半不需要

**2）隐身模式访问（最有效）**
- 能访问 → 不需要 Cookie
- 401/403 → 必须登录 Cookie

**3）URL 是否涉及个人数据**
- 如 `/interact_api/v1/message/count` → 必须登录

**4）响应内容提示**
- 如 `"must login"` → 必须 Cookie

### 你已经成功判断：

- **搜索接口**：公开 API，不需要 Cookie
- **消息计数接口**：私有 API，需要 Cookie，否则 403

## 6. Day02 实战：掘金分页爬虫（cursor-based）

### ✔ cursor 来自服务器，不是本地 cursor+=20

真实分页结构：

```json
{
  "data": [...],
  "cursor": "20_2025xxxx",
  "has_more": true
}
```

### ✔ 正确分页逻辑

```python
cursor = "0"

while True:
    resp = requests.get(url, params={"cursor": cursor})
    data = resp.json()

    for item in data["data"]:
        print(解析内容)

    cursor = data["cursor"]
    has_more = data["has_more"]
    if not has_more:
        break
```

### 你已经跑通：

- **第一页**：cursor = `"0"`
- **第二页**：cursor = `"20_xxx"`
- **第三页**：cursor = `"40_xxx"`
- **……直到** has_more=False

这是现代 API 常见分页方式，掌握它你就能爬知乎、小红书、淘宝评论等。

## 7. Cookie 登录接口初识（预备知识）

你今天还观察到一个关键现象：

```json
{ "err_no": 403, "err_msg": "must login" }
```

### 说明：

- **搜索 API** → 公共，无需 Cookie
- **消息 API** → 私有，需要登录态 Cookie

你还成功抓取了完整的 Cookie 字符串，但尚未成功调用 → 这是明天 Day03 的内容：

- 如何使用 Cookie 调用登录接口？
- 如何从浏览器自动提取 Cookie？
- 如何处理掘金的 CSRF Token？

**我们明天继续。**

## 8. 今日掌握能力总结（Day02）

- ✔ 正确复现 GET / POST 请求
- ✔ 理解 params/data/json 的区别
- ✔ 掌握常用 Header，能识别哪些是反爬关键
- ✔ Session 自动管理 Cookie 与连接
- ✔ 会判断接口是否需要 Cookie
- ✔ 能用 Python 访问必须登录的接口（明天继续突破）
- ✔ 会处理 cursor-based API 分页逻辑
- ✔ 完成一个真实爬虫工程的分页功能