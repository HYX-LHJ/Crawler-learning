# Day09 学习总结

## 一、核心目标达成情况

Day09 的目标是让你从"只能用 Selenium 抓"迈向"用 Selenium 拿登录态，用 requests 批量抓取"的工程方案。

你已经掌握了：

- Selenium 与 requests 的正确分工（身份获取 vs 数据抓取）
- Cookie 的获取前提与生命周期（必须访问域名后才有 cookies）
- 将浏览器 cookies 注入 requests.Session 的标准姿势
- 503 等拦截场景下的 headers 补全策略（User-Agent）
- 形成"会话容器"思维：Session 负责长期状态维护

这是从脚本走向系统的关键一步。

## 二、你已经真正掌握的三大工程能力

### 1. 身份获取与数据抓取解耦（架构能力）

你形成的正确架构是：

```
Selenium 登录/加载（低频）
   ↓
导出 cookies
   ↓
requests.Session（高频请求）
```

你也能明确排除错误方案：

- 每次请求都 Selenium 登录：成本高、稳定性差
- 全程 Selenium 抓取：复杂度高、吞吐差

这属于工程选型能力，而不是代码技巧。

### 2. Cookie 获取的关键前置条件（踩坑后掌握）

你明确了一个非常重要的规则：

- `driver.get_cookies()` 不是"读文件夹"
- 必须先 `driver.get("https://www.amazon.com")` 进入域名上下文，cookies 才会被加载/写入
- 这让你理解了"cookie 是浏览器会话状态"，不是静态文件。

### 3. Session 注入与反爬基础对抗（可用性能力）

你跑通了：

- 将 cookies 转成 `{name: value}` 注入 session
- `session.headers.update({...User-Agent...})` 解决 503
- 理解了 headers/cookies 组合决定请求是否像"真实浏览器"

这使得后续的接口抓取具备可用性基础。

## 三、Day09 实战成果

你完成了从"浏览器登录态"到"requests 复用态"的闭环：

- Selenium 登录成功
- requests 能带着登录态访问目标页面/接口
- 能定位并修复 503（UA 不足导致的拒绝）

这标志着你已经具备"工程级抓取骨架"。

## 四、Day09 完成后的能力等级

**架构能力：Level Up**
- 从"全靠 Selenium" → "Selenium 身份 + requests 批量"

**会话能力：Level Up**
- 从"单次请求" → "Session 维护长期状态"

**可用性能力：Level Up**
- 从"请求被拒" → "能补齐 headers/cookies 使其可用"
