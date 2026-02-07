#!/usr/bin/env python3
rgb = ['Red', 'Green', 'Blue']
rgba = rgb
print(id(rgb) == id(rgba))  # they refer to the same object
rgba.append('Alph')
print(rgba, rgba)  # both will have Alph
correct_rgba = rgba[:]  # shallow copy
correct_rgba[-1] = 'Alpha' # only updates itself, since it is a shallow copy
print(correct_rgba, rgba)

test_variable = {'Red': 'test'}
shallow_copy_proof = [test_variable, 1]
shallow_copy_proof_copy = shallow_copy_proof[:]
shallow_copy_proof_copy[-1] = 2
print(shallow_copy_proof, shallow_copy_proof_copy)
shallow_copy_proof[0]['Green'] = 'new_test'  # the original test_variable is updated itself, so all references to it will change
print(shallow_copy_proof, shallow_copy_proof_copy)
