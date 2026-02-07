#!/usr/bin/env python3
# This program illustrates the uses of else clauses on loops
# more specifically if a break is not executed, then the else executes, here's an example of a prime number finding program
import sys
import math

def main() -> None:
    if len(sys.argv) != 2:
        print('Usage ./els_clauses_on_loops.py NUMBER')
        sys.exit(1)
    try:
        specify_all_primes_until(int(sys.argv[1]))
    except TypeError:
        print('Please enter an integer')
        sys.exit(2)


def specify_all_primes_until(n: int) -> None:
    for i in range(2, n + 1):
        is_prime(i)


def is_prime(n: int) -> None:
    for elem in range(2, int(math.sqrt(n)) + 1):
        if n % elem == 0:
            print(f'{n} equals {elem} * {n // elem}')
            break
    else:
        print(f'{n} is a prime number')
    
    
        
    
    
    
if __name__ == "__main__":
    main()
