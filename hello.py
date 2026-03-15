#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
小叮当测试脚本
用于演示 GitHub 代码提交功能
"""

import datetime


def greet(name: str) -> str:
    """向用户问好"""
    return f\"你好，{name}！我是小叮当 🤖\"


def get_current_time() -> str:
    """获取当前时间"""
    return datetime.datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")


def main():
    print(\"=\" * 40)
    print(greet(\"李老板\"))
    print(f\"当前时间: {get_current_time()}\")
    print(\"=\" * 40)
    print(\"\\n这是小叮当创建的测试代码文件\")
    print(\"仓库: liyuhui666/xiao-ding-dang-test\")


if __name__ == \"__main__\":
    main()