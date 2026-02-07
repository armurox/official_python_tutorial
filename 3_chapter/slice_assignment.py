#!/usr/bin/env python3
# while slicing generates a shallow copy, slice assignment still works
list = ['a', 'b', 'c']
print(list)
list[3:5] = ['d', 'e']
print(list)
list[:] = []
print(list)