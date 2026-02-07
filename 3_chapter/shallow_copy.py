#!/usr/bin/env python3
rgb = ['Red', 'Green', 'Blue']
rgba = rgb
print(id(rgb) == id(rgba))  # they refer to the same object
rgba.append('Alph')
print(rgba, rgba)  # both will have Alph
correct_rgba = rgba[:]  # shallow copy
correct_rgba[-1] = 'Alpha' # only updates itself, since it is a shallow copy
print(correct_rgba, rgba)
