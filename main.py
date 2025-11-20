#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Screen2PDF - Online Document Downloader / 在线文档下载器

Description / 项目描述:
A Python tool to capture screenshots of online documents (like Feishu/Lark, etc.) 
and convert them into a single PDF file. 
这是一个用于抓取在线文档（如飞书/Lark等）截图并将其转换为 PDF 文件的 Python 工具。

It supports automatic driver detection and runs in a "silent mode" to keep the console clean.
它支持自动检测浏览器驱动，并以“静默模式”运行以保持控制台整洁。

Features / 功能特性:
1. Auto-detects browser drivers (Edge/Chrome).
   自动检测浏览器驱动（支持 Edge 和 Chrome）。
2. "Silent Mode" - Suppresses annoying browser logs.
   “静默模式” - 屏蔽烦人的浏览器底层日志。
3. Optimized for stability - Prevents page skipping during screenshots.
   稳定性优化 - 防止截图过程中的跳页问题。
4. Converts screenshots to PDF automatically.
   自动将截图合并为 PDF 文件。
5. Bilingual Support (English/Chinese).
   双语支持（英文/中文）。

Author: Z-Teddy (Z-Teddy)
GitHub: https://github.com/Z-Teddy/Screen2PDF
License: MIT
"""

import os
import re
import time
import platform
import webbrowser
import subprocess
from typing import List, Dict

from PIL import Image
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# ======================== Localization / 多语言配置 ========================

class Lang:
    """
    Handles bilingual text resources.
    处理双语文本资源
    """
    CN = {
        'select_lang': "请选择语言 / Please select language:\n  [1] 中文 (默认)\n  [2] English",
        'select_browser': "请选择浏览器:",
        'browser_edge': "  [1] Edge (默认)",
        'browser_chrome': "  [2] Chrome",
        'input_num': "\n请输入数字 (默认 1): ",
        'input_url': "\n🔗 请输入文档链接: ",
        'invalid_url': "❌ 无效的 URL",
        'driver_detected': "🔍 检测到驱动: {}",
        'driver_missing': "\n❌ 未检测到 {} 驱动！\n",
        'driver_guide_1': "请按照以下步骤手动下载驱动：",
        'driver_guide_2_chrome': "1. 在 Chrome 地址栏输入: chrome://version 查看版本号",
        'driver_guide_2_edge': "1. 在 Edge 地址栏输入: edge://settings/help 查看版本号",
        'driver_guide_3': "2. 前往官方下载页: {}",
        'driver_guide_4': "3. 下载对应版本的驱动 (zip包)，解压后将 exe 文件放到:\n   👉 {}",
        'open_web_prompt': "\n提示: 是否自动打开下载页面？(Y/n)",
        'restart_hint': "请配置好驱动后重新运行程序。",
        'browser_started': "✓ {} 浏览器启动成功\n",
        'driver_fail': "\n❌ 驱动启动失败: {}",
        'driver_ver_mismatch': "可能是驱动版本与浏览器版本不匹配，请重新下载对应版本的驱动。",
        'processing': "\n🚀 开始处理: {}",
        'wait_load': "⏳ 等待页面加载（10秒）...",
        'doc_info_title': "\n📝 文档信息",
        'input_title': "请输入文档标题: ",
        'input_pages': "请输入总页数: ",
        'invalid_num': "❌ 请输入有效数字",
        'prep_title': "\n🎬 准备截图",
        'prep_1': "1. 请手动进入演示/全屏模式",
        'prep_2': "2. 确保当前显示第 1 页",
        'prep_3': "   (请勿手动点击页面，以免误触发翻页)",
        'press_enter': "\n完成后按回车键开始截图...",
        'stabilizing': "⏳ 正在稳定全屏焦点，请稍候 3 秒...",
        'capturing': "\n📸 开始截图 (共 {} 页)...",
        'flip_fail': "⚠️ 翻页失败，请手动翻到第 {} 页并回车...",
        'gen_pdf': "\n🔄 正在生成 PDF...",
        'no_img': "❌ 未找到图片文件",
        'merging': "\n📦 准备合并 {} 张图片...",
        'loaded': "  ✓ 已加载: {}",
        'load_fail': "  ✗ 加载失败 {}: {}",
        'no_valid_img': "❌ 没有可用的图片",
        'pdf_saved': "\n✅ PDF 已保存: {}",
        'total_pages': "✅ 共 {} 页",
        'save_fail': "❌ 保存 PDF 失败: {}",
        'cleaning': "\n🗑️  清理资源，程序退出。",
        'exit_prompt': "按回车键退出...",
        'error_generic': "\n❌ 发生错误: {}"
    }

    EN = {
        'select_lang': "Please select language / 请选择语言:\n  [1] Chinese (Default)\n  [2] English",
        'select_browser': "Select Browser:",
        'browser_edge': "  [1] Edge (Default)",
        'browser_chrome': "  [2] Chrome",
        'input_num': "\nEnter number (Default 1): ",
        'input_url': "\n🔗 Enter Document URL: ",
        'invalid_url': "❌ Invalid URL",
        'driver_detected': "🔍 Driver detected: {}",
        'driver_missing': "\n❌ Driver not found for {}!\n",
        'driver_guide_1': "Please follow these steps to set up the driver:",
        'driver_guide_2_chrome': "1. Check Chrome version: enter `chrome://version` in address bar.",
        'driver_guide_2_edge': "1. Check Edge version: enter `edge://settings/help` in address bar.",
        'driver_guide_3': "2. Download driver from: {}",
        'driver_guide_4': "3. Unzip and place the executable file here:\n   👉 {}",
        'open_web_prompt': "\nTip: Open download page now? (Y/n)",
        'restart_hint': "Please restart the program after setting up the driver.",
        'browser_started': "✓ {} started successfully.\n",
        'driver_fail': "\n❌ Failed to start driver: {}",
        'driver_ver_mismatch': "Ensure the driver version matches your browser version.",
        'processing': "\n🚀 Processing: {}",
        'wait_load': "⏳ Waiting for page load (10s)...",
        'doc_info_title': "\n📝 Document Info",
        'input_title': "Enter document title: ",
        'input_pages': "Enter total pages: ",
        'invalid_num': "❌ Invalid input. Please enter a number.",
        'prep_title': "\n🎬 Preparation",
        'prep_1': "1. Please manually switch to Presentation/Full Screen mode.",
        'prep_2': "2. Ensure page 1 is displayed.",
        'prep_3': "   (Do NOT click the page manually to avoid accidental flipping)",
        'press_enter': "\nPress Enter when ready to start capturing...",
        'stabilizing': "⏳ Stabilizing focus (3s)...",
        'capturing': "\n📸 Capturing ({} pages)...",
        'flip_fail': "⚠️ Flip failed. Please manually flip to page {} and press Enter...",
        'gen_pdf': "\n🔄 Generating PDF...",
        'no_img': "❌ No image files found",
        'merging': "\n📦 Merging {} images...",
        'loaded': "  ✓ Loaded: {}",
        'load_fail': "  ✗ Failed to load {}: {}",
        'no_valid_img': "❌ No valid images available",
        'pdf_saved': "\n✅ PDF Saved: {}",
        'total_pages': "✅ Total Pages: {}",
        'save_fail': "❌ Failed to save PDF: {}",
        'cleaning': "\n🗑️  Cleaning up resources. Exit.",
        'exit_prompt': "Press Enter to close...",
        'error_generic': "\n❌ Error: {}"
    }

    current = CN  # Default to Chinese / 默认为中文

    @classmethod
    def set_lang(cls, lang_code):
        if lang_code == '2':
            cls.current = cls.EN
        else:
            cls.current = cls.CN

    @classmethod
    def get(cls, key, *args):
        text = cls.current.get(key, key)
        if args:
            return text.format(*args)
        return text


# ======================== Configuration / 配置常量 ========================

DRIVER_LINKS = {
    'chrome': 'https://googlechromelabs.github.io/chrome-for-testing/',
    'edge': 'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/'
}

# ======================== Utils / 工具函数 ========================

def clean_title(original_title: str) -> str:
    if not original_title or not original_title.strip():
        return f"document_{int(time.time())}"
    illegal_chars = r'[\\/:*?"<>|]'
    cleaned = re.sub(illegal_chars, '', original_title)
    if cleaned.lower().endswith('.pdf'):
        cleaned = cleaned[:-4]
    return cleaned.strip() or f"document_{int(time.time())}"


def merge_images_to_pdf(folder_path: str, output_pdf_path: str) -> bool:
    supported_formats = {'.jpg', '.jpeg', '.png', '.webp'}
    image_files = [
        f for f in os.listdir(folder_path)
        if os.path.splitext(f)[1].lower() in supported_formats
    ]
    
    def extract_number(filename: str) -> int:
        nums = re.findall(r'\d+', filename)
        return int(nums[0]) if nums else 0
    
    image_files.sort(key=extract_number)
    
    if not image_files:
        print(Lang.get('no_img'))
        return False
    
    print(Lang.get('merging', len(image_files)))
    
    images = []
    for filename in image_files:
        img_path = os.path.join(folder_path, filename)
        try:
            with Image.open(img_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                images.append(img.copy())
            print(Lang.get('loaded', filename))
        except Exception as e:
            print(Lang.get('load_fail', filename, e))
    
    if not images:
        print(Lang.get('no_valid_img'))
        return False
    
    try:
        images[0].save(
            output_pdf_path,
            'PDF',
            save_all=True,
            append_images=images[1:]
        )
        print(Lang.get('pdf_saved', output_pdf_path))
        print(Lang.get('total_pages', len(images)))
        return True
    except Exception as e:
        print(Lang.get('save_fail', e))
        return False
    finally:
        for img in images:
            img.close()


# ======================== Driver Management / 驱动管理 ========================

def get_driver_path(browser: str) -> str:
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    paths = {
        'chrome': {
            'windows': 'chrome_win64/chromedriver.exe',
            'darwin_arm': 'chrome_mac_arm64/chromedriver',
            'darwin_x86': 'chrome_mac_x64/chromedriver',
            'linux': 'chrome_linux64/chromedriver'
        },
        'edge': {
            'windows': 'edge_win64/msedgedriver.exe'
        }
    }

    if 'windows' in system: os_key = 'windows'
    elif 'darwin' in system: os_key = 'darwin_arm' if 'arm' in machine else 'darwin_x86'
    elif 'linux' in system: os_key = 'linux'
    else: return None

    if browser not in paths or os_key not in paths[browser]:
        return None
        
    return os.path.join('drivers', paths[browser][os_key])


def show_download_guide(browser: str, target_path: str):
    print(f"\n{'='*60}")
    print(Lang.get('driver_missing', browser.capitalize()))
    print(f"{'='*60}\n")
    
    print(Lang.get('driver_guide_1'))
    
    if browser == 'chrome':
        print(Lang.get('driver_guide_2_chrome'))
    else:
        print(Lang.get('driver_guide_2_edge'))
    
    print(Lang.get('driver_guide_3', DRIVER_LINKS[browser]))
    
    abs_path = os.path.abspath(target_path)
    print(Lang.get('driver_guide_4', abs_path))
    
    choice = input(Lang.get('open_web_prompt') + " ").strip().lower()
    if choice not in ['n', 'no']:
        webbrowser.open(DRIVER_LINKS[browser])
    
    raise FileNotFoundError(Lang.get('restart_hint'))


def init_driver(browser: str) -> WebDriver:
    driver_path = get_driver_path(browser)
    
    if not driver_path or not os.path.exists(driver_path):
        show_download_guide(browser, driver_path or "drivers/...")
        return None

    print(Lang.get('driver_detected', driver_path))
    
    try:
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            service_cls = webdriver.ChromeService
        else:
            options = webdriver.EdgeOptions()
            service_cls = webdriver.EdgeService

        options.add_argument('--start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        
        # Silent mode settings
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        options.add_argument("--disable-logging")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        service = service_cls(
            executable_path=driver_path, 
            log_output=subprocess.DEVNULL 
        )
        
        if browser == 'chrome':
            driver = webdriver.Chrome(service=service, options=options)
        else:
            driver = webdriver.Edge(service=service, options=options)
        
        print(Lang.get('browser_started', browser.capitalize()))
        return driver

    except Exception as e:
        print(Lang.get('driver_fail', e))
        print(Lang.get('driver_ver_mismatch'))
        raise


# ======================== Core Logic / 核心逻辑 ========================

class DocumentDownloader:
    def __init__(self, driver: WebDriver, url: str, output_dir: str):
        self.driver = driver
        self.url = url
        self.output_dir = output_dir
    
    def run(self):
        print(f"{'='*60}")
        print(Lang.get('processing', self.url))
        print(f"{'='*60}")
        
        self.driver.get(self.url)
        print(Lang.get('wait_load'))
        time.sleep(10)
        
        print(f"{'='*60}")
        print(Lang.get('doc_info_title'))
        print(f"{'='*60}")
        
        title = input(Lang.get('input_title')).strip()
        title = clean_title(title)
        
        while True:
            try:
                total_pages = int(input(Lang.get('input_pages')).strip())
                if total_pages > 0: break
            except: pass
            print(Lang.get('invalid_num'))
            
        folder_path = os.path.join(self.output_dir, title)
        os.makedirs(folder_path, exist_ok=True)
        
        print(f"{'='*60}")
        print(Lang.get('prep_title'))
        print(f"{'='*60}")
        print(Lang.get('prep_1'))
        print(Lang.get('prep_2'))
        print(Lang.get('prep_3'))
        input(Lang.get('press_enter'))
        
        try:
            ActionChains(self.driver).move_by_offset(0, 0).perform()
        except: pass
        
        print(Lang.get('stabilizing'))
        time.sleep(3) 
        
        print(Lang.get('capturing', total_pages))
        
        for page in range(1, total_pages + 1):
            time.sleep(2.0)
            
            img_path = os.path.join(folder_path, f"{page}.png")
            self.driver.save_screenshot(img_path)
            print(f"  ✓ Page {page}/{total_pages}")
            
            if page < total_pages:
                try:
                    ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
                except:
                    input(Lang.get('flip_fail', page+1))
        
        print(Lang.get('gen_pdf'))
        pdf_path = os.path.join(self.output_dir, f"{title}.pdf")
        merge_images_to_pdf(folder_path, pdf_path)


# ======================== Main / 主程序 ========================

def main():
    print("=" * 60)
    print("S C R E E N   2   P D F".center(54))
    print("=" * 60)
    
    # Language Selection
    print(Lang.CN['select_lang'])
    lang_choice = input("\n> ").strip()
    Lang.set_lang(lang_choice)
    
    print("\n" + Lang.get('select_browser'))
    print(Lang.get('browser_edge'))
    print(Lang.get('browser_chrome'))
    
    choice = input(Lang.get('input_num')).strip()
    browser = 'chrome' if choice == '2' else 'edge'
    
    url = input(Lang.get('input_url')).strip()
    if not url.startswith('http'):
        return print(Lang.get('invalid_url'))
    
    output_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    driver = None
    try:
        driver = init_driver(browser)
        if driver:
            downloader = DocumentDownloader(driver, url, output_dir)
            downloader.run()
    
    except FileNotFoundError as e:
        print(f"\n⚠️  {e}")
    except Exception as e:
        print(Lang.get('error_generic', e))
    finally:
        if driver:
            driver.quit()
            print(Lang.get('cleaning'))
        input(Lang.get('exit_prompt'))

if __name__ == '__main__':
    main()