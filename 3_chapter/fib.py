#!/usr/bin/env python3
# a nice little program for fibonacci computation
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: ./fib.py NUMBER')
        sys.exit(1)
    try:
        fib(int(sys.argv[1]))
    except TypeError:
        print('Please enter an integer')
        sys.exit(2)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


if __name__ == "__main__":
    main()

    