#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: ./fib2.py NUMBER')
        sys.exit(1)
    # Get value and convert it into an argument
    while True:
        try:
            result = fib(int(sys.argv[1]))
            break
        except ValueError as e:
            print(e.args[0])
    print(result)


def fib(n):
    a, b = 0, 1
    result = []
    for _ in range(1, n + 1):
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    main()
