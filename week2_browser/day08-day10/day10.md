# Day10 学习总结

## 一、核心目标达成情况

Day10 的目标是把 Day08（接口）+ Day09（登录态）整合成一个"可运行、可扩展"的实战爬虫闭环：Amazon 评论多页抓取。

你已经掌握了：

- 第 1 页 HTML 解析 + 第 2 页起 AJAX 接口抓取的组合策略
- Amazon 评论接口返回为 &&& 指令流的解析方法
- GET 必须使用 params（而不是 data）才能正确传参
- 统一的评论解析入口（从 HTML 还原为结构化数据）
- cookies 本地落盘复用，避免每次启动 Selenium

这基本就是"生产雏形"。

## 二、你已经真正掌握的三大工程能力

### 1. 非标准响应解析能力（&&& 指令流）

你理解并跑通了 Amazon 的返回形态：

- Response 不是 JSON
- 而是 &&& 分隔的指令块
- 其中包含 `["append", "#cm_cr-review_list", "<li...>"]`

你实现了标准解析链路：

```
split → json.loads → 过滤 append → 拼接 HTML → Soup 解析 li[data-hook="review"]
```

这是动态网站抓取里非常典型也非常值钱的能力。

### 2. 请求语义正确性（GET params vs data）

你明确掌握：

- `session.get(..., params=payload)` ✅
- `session.get(..., data=payload)` ❌（GET 不会带上 querystring）

这是很多"请求能发出但拿不到数据"的根因，你已经能一眼定位。

### 3. 工程化闭环：cookies 本地化与复用

你完成了"降成本"升级：

- 第一次：Selenium 拿 cookies → 保存本地文件
- 后续：直接读本地 cookies → 注入 session → 抓取

这一步让脚本从"调试版"走向"可长期运行的工具"。

## 三、Day10 实战成果

你最终跑通并验证了：

- 第 1 页能解析出 10 条评论
- 第 2 页起能通过接口拉取并解析评论
- 最终返回结构化评论数据（title/body/rating 等）

整体闭环可运行，并且已经具备扩展到多页/批量 ASIN 的能力

这意味着 Week2 的核心目标已经完成：从"会爬"到"能做工具"。

## 四、Day10 完成后的能力等级

**解析能力：Level Up**
- 从"只会 parse HTML" → "能解析指令流并还原 DOM"

**稳定性能力：Level Up**
- 从"偶尔能跑" → "知道参数/headers/cookies 的必要性与正确性"

**工程化能力：Level Up**
- 从"单次脚本" → "cookies 本地复用 + 可扩展闭环"
