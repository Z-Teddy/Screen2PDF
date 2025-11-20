# Screen2PDF  📄 ➡️ 📂

[English](#english) | [中文](#chinese)

---
<span id="english"></span>

## 🇺🇸 English Description

**Screen2PDF** is a lightweight, automated Python tool designed to "download" online presentation documents (such as **Feishu/Lark Docs**, Google Slides, etc.) that do not provide a native download button.

It works by automatically taking high-quality screenshots of each page in the browser and then intelligently merging them into a single PDF file.

### ✨ Key Features

-  **🌍 Bilingual Interface**: Full support for both **English** and **Chinese** environments.
-  **🚀 Auto Driver Detection**: Automatically detects and configures drivers for **Microsoft Edge** and **Google Chrome**.
-  **🔇 Silent Mode**: Runs the browser driver in silent mode, suppressing annoying console logs for a clean experience.
-  **📄 Smart Conversion**: Automatically captures screenshots and merges them into a PDF file without manual intervention.
-  **🛡️ Stability Optimized**: Includes mechanisms to prevent page skipping during the capture process.

### 📦 Prerequisites

Before running the script, please ensure you have the following installed:

- **Python 3.x**
- **Google Chrome** or **Microsoft Edge** browser

### 🛠️ Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/Z-Teddy/Screen2PDF.git  cd Screen2PDF  
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

     *(If* *`requirements.txt`* *is missing, manually install:*  *`pip install selenium Pillow`* *)*
3. **Browser Drivers (Important)** The project contains a pre-made drivers folder structure. Please download the matching driver for your browser version:

    - **Chrome**: [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
    - **Edge**: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

    **Then, simply place the driver executable (e.g.,**  **`msedgedriver.exe`** **) into the corresponding folder:**
   
    - For Edge (Windows): Put it in `drivers/edge_win64/`
    - For Chrome (Windows): Put it in `drivers/chrome_win64/`

### 🚀 Usage

Run the main script:

```bash
python main.py
```

Follow the on-screen instructions:

1. Select language (Chinese/English).
2. Select your browser (Edge/Chrome).
3. Paste the URL of the document you want to capture.
4. Enter the document title and total number of pages.
5. **Switch the browser to "Presentation/Full Screen" mode manually** when prompted, then press Enter.

The final PDF will be saved to your **Desktop**.

---

<span id="chinese"></span>

## 🇨🇳 中文说明

**Screen2PDF** 是一个轻量级的 Python 自动化工具，旨在解决无法直接下载在线演示文档（如 **飞书/Lark 文档**、PPT 等）的问题。

它的工作原理是自动对浏览器中的每一页文档进行高清截图，然后智能地将这些图片合并成一个完整的 PDF 文件。

### ✨ 核心功能

-  **🌍 双语界面**：完全支持 **中文** 和 **英文** 交互界面。
-  **🚀 自动驱动检测**：支持自动检测并配置 **Microsoft Edge** 和 **Google Chrome** 的浏览器驱动。
-  **🔇 静默模式**：以静默模式运行浏览器驱动，屏蔽烦人的底层日志输出，界面更清爽。
-  **📄 智能转换**：全自动截图并合并为 PDF，无需手动操作图片。
-  **🛡️ 稳定性优化**：内置防跳页机制，确保截图过程稳定流畅。

### 📦 准备工作

在运行脚本之前，请确保您的电脑已安装：

- **Python 3.x**
- **Google Chrome** 或 **Microsoft Edge** 浏览器

### 🛠️ 安装步骤

1. **克隆项目**

    ```bash
    git clone https://github.com/Z-Teddy/Screen2PDF.git
    cd Screen2PDF
    ```
2. **安装依赖库**

    ```bash
    pip install -r requirements.txt
    ```

     *(如果没有 requirements.txt，请手动运行：**`pip install selenium Pillow`* *)*
3. **关于浏览器驱动 (重要)** 项目中已为您预设了 drivers 文件夹结构。请根据您的浏览器版本下载对应的驱动：

    - **Chrome**: [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
    - **Edge**: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

    **下载解压后，直接将驱动文件（如** **`msedgedriver.exe`** **）放入对应的文件夹即可：**

    - Edge (Windows): 放入 `drivers/edge_win64/` 文件夹
    - Chrome (Windows): 放入 `drivers/chrome_win64/` 文件夹

### 🚀 使用方法

运行主程序：

```bash
python main.py
```

根据屏幕提示操作：

1. 选择语言（中文/英文）。
2. 选择浏览器（Edge/Chrome）。
3. 粘贴您想要抓取的文档链接。
4. 输入文档标题和总页数。
5. 当提示准备截图时，**请手动将浏览器切换至“演示/全屏”模式**，然后按回车开始。

生成的 PDF 文件将默认保存在您的 **桌面**。

---

## ⚠️ Disclaimer / 免责声明

**English:**

1. **Educational Use Only**: This tool is intended for **personal learning and research purposes only**.
2. **Copyright Respect**: Please strictly adhere to the copyright laws of your country/region. Do not use this tool to download, share, or distribute copyright-protected documents without authorization.
3. **User Responsibility**: The author holds no responsibility for any legal consequences or damages resulting from the improper use of this tool. All actions and consequences are the sole responsibility of the user.
4. **Platform Terms**: Users should comply with the Terms of Service (ToS) of the target platforms (e.g., Feishu/Lark, Google Slides).
5. **No Warranty**: This software is provided "as is", without warranty of any kind.

**中文:**

1. **仅供学习**：本工具仅供**个人学习和研究使用**，请勿用于商业用途。
2. **尊重版权**：请严格遵守所在国家或地区的版权法律法规。未经授权，请勿下载、传播或分发受版权保护的文档。
3. **责任自负**：因使用本工具而产生的任何法律后果或损失（包括但不限于版权侵权、账号封禁等），均由用户自行承担，作者不承担任何责任。
4. **遵守规则**：用户应遵守目标平台（如飞书、Google Slides 等）的服务条款（ToS）。
5. **无担保**：本软件按“原样”提供，不提供任何形式的明示或暗示担保。

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

**Z-Teddy**
GitHub: [@Z-Teddy](https://github.com/Z-Teddy)

