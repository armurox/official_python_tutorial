# Program to illustrate access to __annotations__ of a function
def f(ham: str, eggs: str = 'eggs') -> str:
    print('Annotations', f.__annotations__)
    print('Arguments', eggs, ham)
    return 'Green' + eggs + ' and ' + ham
print(f('ham'))
