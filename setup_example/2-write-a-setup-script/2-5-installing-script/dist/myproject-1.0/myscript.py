#!/usr/bin/env python
# myscript.py - Không cần import từ package
import sys


def greet(name):
    return f"Hello, {name}!"


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(name))


if __name__ == '__main__':
    main()