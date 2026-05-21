#!/usr/bin/env python3

import sys
import os

def print_colored_ascii(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换 ANSI 颜色代码
    color_map = {
        '\\033[31m': '\033[31m',  # 红色
        '\\033[32m': '\033[32m',  # 绿色
        '\\033[33m': '\033[33m',  # 黄色
        '\\033[34m': '\033[34m',  # 蓝色
        '\\033[35m': '\033[35m',  # 紫色
        '\\033[36m': '\033[36m',  # 青色
        '\\033[0m': '\033[0m',    # 重置
    }

    for escaped, actual in color_map.items():
        content = content.replace(escaped, actual)

    print(content)

def print_sample_ascii():
    """打印示例彩色ASCII艺术字"""
    samples = {
        'A': [
            '\033[31m    ██████╗ ██████╗ ███████╗███████╗████╗ ████╗███████╗',
            '\033[32m   ██╔════╝██╔═══██╗██╔════╝██╔══██╗████╗ ████║██╔════╝',
            '\033[33m   ██║     ██║   ██║█████╗  ███████║██╔████╔██║███████╗',
            '\033[34m   ██║     ██║   ██║██╔══╝  ██╔══██║██║╚██╔╝██║╚════██║',
            '\033[35m   ╚██████╗╚██████╔╝███████╗██║  ██║██║ ╚═╝ ██║███████║',
            '\033[36m    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝\033[0m'
        ],
        'Y': [
            '\033[31m   ██╗  ██╗██╗██╗██╗██╗  ███████╗██████╗ ',
            '\033[32m   ██║  ██║██║██║██║██║  ██╔════╝██╔══██╗',
            '\033[33m   ███████║██║██║██║██║  ███████╗██████╔╝',
            '\033[34m   ██╔══██║██║██║██║██║  ╚════██║██╔══██╗',
            '\033[35m   ██║  ██║██║██║██║████╗███████║██║  ██║',
            '\033[36m   ╚═╝  ╚═╝╚═╝╚═╝╚═╝╚═══╝╚══════╝╚═╝  ╚═╝\033[0m'
        ],
        'C': [
            '\033[31m    ██████╗ ██████╗ ██████╗ ███████╗',
            '\033[32m   ██╔════╝██╔═══██╗██╔══██╗██╔════╝',
            '\033[33m   ██║     ██║   ██║██║  ██║█████╗  ',
            '\033[34m   ██║     ██║   ██║██║  ██║██╔══╝  ',
            '\033[35m   ╚██████╗╚██████╔╝██████╔╝███████╗',
            '\033[36m    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝\033[0m'
        ],
        '3': [
            '\033[31m    █████╗  ██████╗ ██████╗ ███████╗',
            '\033[32m   ██╔════╝██╔═══██╗██╔══██╗██╔════╝',
            '\033[33m   ██║     ██║   ██║██║  ██║█████╗  ',
            '\033[34m   ██║     ██║   ██║██║  ██║██╔══╝  ',
            '\033[35m   ╚██████╗╚██████╔╝██████╔╝███████╗',
            '\033[36m    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝\033[0m'
        ]
    }

    print("\n" + "="*80)
    print("YYC³ 彩色ASCII艺术字示例")
    print("="*80 + "\n")

    for letter, lines in samples.items():
        print(f"\n## {letter}\n")
        for line in lines:
            print(line)
        print()

def print_all_letters():
    """打印所有字母A-Z"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("\n" + "="*80)
    print("YYC³ A-Z 彩色ASCII艺术字")
    print("="*80 + "\n")

    for i, char in enumerate(alphabet, 1):
        print(f"\n## {char}\n")
        # 使用不同的颜色模式
        colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']
        for j, color in enumerate(colors):
            print(f"{color}   {'█' * 20}\033[0m")
        print()

def print_all_numbers():
    """打印所有数字0-9"""
    print("\n" + "="*80)
    print("YYC³ 0-9 彩色ASCII艺术字")
    print("="*80 + "\n")

    for i in range(10):
        print(f"\n## {i}\n")
        colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']
        for j, color in enumerate(colors):
            print(f"{color}   {'█' * 20}\033[0m")
        print()

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            print_colored_ascii(file_path)
        else:
            print(f"错误：文件 '{file_path}' 不存在")
            sys.exit(1)
    else:
        print_sample_ascii()
        print("\n" + "="*80)
        print("提示：使用 'python3 YYC3-ASCII艺术字.py <文件路径>' 查看完整的彩色ASCII艺术字文件")
        print("="*80)

if __name__ == '__main__':
    main()
