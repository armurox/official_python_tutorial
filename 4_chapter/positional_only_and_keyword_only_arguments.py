#!/usr/bin/env python3
def main():
    print(foo('hello', **{"name": 30}))
    try:
        print(foo_keyword_only(2, 1))
    except TypeError as e:
        print(e.args[0])
    

def foo(name, /, **kwargs):
    return name, 'name' in kwargs

def foo_keyword_only(num, /, *, name):  # one positional only, and then one keyword only argument expected
    return num, name
    
    
if __name__ == '__main__':
    main()
