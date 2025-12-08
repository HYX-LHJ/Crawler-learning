# Week2 · Day06 学习总结 — Selenium 环境准备与基础浏览器控制

## 1. Selenium 基础与运行机制理解

Selenium 本质上不能直接控制 Chrome 浏览器。

Chrome 只能接受 DevTools Protocol 指令，而 Selenium 无法直接发送这些指令。

因此需要 chromedriver 作为中间层，将 Selenium 的命令翻译为浏览器的执行指令。

**关系模型：**

```
Selenium → chromedriver（WebDriver） → Chrome 浏览器
```

## 2. Selenium 4 的标准浏览器启动方式

Selenium 4 开始采用 Service 对象管理浏览器驱动：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
```

**特点：**

- 驱动管理被从 WebDriver 中分离出来，责任更清晰。
- 支持多类型浏览器（Chrome / Edge / Firefox）。
- 推荐写法（旧版本的 `executable_path=` 已被废弃）。

## 3. Selenium 启动后获取网页基本信息（属性访问）

Selenium 中浏览器状态统一通过"属性"获取，而非方法调用：

**获取网页标题：**

```python
driver.title
```

**获取当前 URL：**

```python
driver.current_url
```

**获取页面源码：**

```python
driver.page_source
```

**关键点：**
这些都是属性，不是 `get_title()`、`get_url()` 这种方法。

## 4. 浏览器窗口控制能力

Selenium 提供基础窗口控制 API：

**最大化窗口**

```python
driver.maximize_window()
```

**指定窗口大小**

```python
driver.set_window_size(800, 600)
```

**用途：**

- 适配不同页面布局
- 保证自动化动作在固定窗口尺寸下运行
- 为后面截图、页面渲染测试打基础

## 5. 网页截图功能（自动化必备）

Selenium 支持将当前页面截图保存到本地：

```python
driver.save_screenshot("home.png")
```

**作用：**

- 记录运行状态
- 调试页面加载
- 自动化测试（如 UI 测试、爬虫行为验证）

## 6. Day06 完成的实践任务清单

你已完成：

- 安装 Selenium
- 下载并配置 chromedriver
- 基于 Service 启动 Chrome
- 打开网页（Google）
- 获取标题与 URL
- 操作窗口（maximize + resize）
- 截图保存
- 完整构建了第一个自动化浏览器脚本

Selenium 环境已经完全可用，可以进入下一阶段的浏览器交互。

## Day06 学习收获总结（核心认知）

- chromedriver 是 Selenium 的必需组件，它负责执行浏览器操作。
- Selenium 4 推荐使用 Service 来管理驱动路径。
- 网页信息多为属性访问，不是方法调用（`driver.title`）。
- 窗口控制和截图是自动化脚本的基础能力。

通过今天的学习，你已经具备运行自动化浏览器的所有基础条件。