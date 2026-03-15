#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Xiao Ding Dang Test Script
Demo for GitHub code submission
Author: Xiao Ding Dang (AI Assistant)
Date: 2026-03-15
"""

import datetime


def greet(name: str) -> str:
    """Greet the user"""
    return f"Hello, {name}! I am Xiao Ding Dang"


def get_current_time() -> str:
    """Get current time"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    print("=" * 40)
    print(greet("Boss Li"))
    print(f"Current time: {get_current_time()}")
    print("=" * 40)
    print("\nThis is a test code file created by Xiao Ding Dang")
    print("Repository: liyuhui666/xiao-ding-dang-test")


if __name__ == "__main__":
    main()