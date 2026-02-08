#!/usr/bin/env python3
def main():
    for i in range(1, 4):
        print(f(i))  # keeps increasing
    
    for i in range(1, 4):
        print(f_correct(i))  # evaluates each value singly


def f(a, L=[]):
    L.append(a)
    return L


def f_correct(a, L=None):
    if L == None:
        L = []
    L.append(a)
    return L
    
    
if __name__ == "__main__":
    main()
