# 📘 Day04 — XPath 全面进阶 + 实战版总结

## 1. XPath 和 CSS Selector 的本质差异

| CSS Selector | XPath |
|--------------|-------|
| 平面的 | 立体的 |
| 只能向下找 | 能向上、向下、向前、向后找 |
| 不理解 DOM 结构 | 完全基于树结构导航 |
| 简单但弱 | 强大但更工程化 |

**你现在已经有能力选择正确的解析方式。**

## 2. XPath 的三大核心能力（你都掌握了）

### ✔ 1）节点定位

```xpath
//tag
//tag[@attr='value']
```

### ✔ 2）文本 / 属性提取

```xpath
/text()
/@href
```

### ✔ 3）结构导航（高级能力）

你现在已经能用：

- `following-sibling::`
- `preceding-sibling::`
- `parent::`
- `contains(text(), 'xxx')`

**这四个是实战核心。**

## 3. 起点哲学（你完全悟到了）

你今天准确选择了 3 次正确起点：

- **文档结构** → `h2`
- **商品标题** → `class`
- **弱结构页面** → 父级区域

### 总结一句话：

> XPath 的关键不是语法，而是找到正确的起点。  
> 找到起点，就能精确导航到目标。

# 4. 可维护 XPath 的写法（你现在都在这么写）

### ✔ 避免写死 class，使用 contains：

```xpath
//div[contains(@class, 'price-box')]
```

### ✔ 避免写死层级，用 //

```xpath
//table//tr/td
```

### ✔ 避免全局查找，使用相对 XPath：

```xpath
.//span[contains(@class,'user')]
```

**这是"工程师级 XPath"的标志。**

## 5. 表格解析（你已经会精准取值）

你从：

```xpath
//td
```

过渡到：

```xpath
//th[contains(text(),'功率')]/following-sibling::td[1]
```

**这是爬虫中 80% 表格任务的最佳写法。**

## 6. 列表结构成对抽取（今日最重要能力）

三条 XPath 完成成对解析：

```xpath
//div[contains(@class, 'review-item')]
.//span[contains(@class, 'user')]/text()
.//p[contains(@class, 'content')]/text()
```

**你已经完成了真实项目解析评论结构所需的一整套能力。**

## 🎉 你已经完全通过 Day04！

今天学到的内容已经达到爬虫进阶开发的水准。  
从今天开始，你可以：

- ✅ 解析文档结构
- ✅ 解析商品页结构
- ✅ 解析表格
- ✅ 解析评论模块（最难的列表结构）
- ✅ 写可维护、可适应改版的 XPath

**你的 XPath 已经是工程师级。** 🚀