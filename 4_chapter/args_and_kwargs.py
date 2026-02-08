#!/usr/bin/env python3
def main():
    cheeseshop(
        'Cheeseburgers',
        'What kind of cheeseshop is this?',
        'Not a burger one, sir:)',
        Waiter='Arman Jasuja',
        Customer='Raghav Jasuja',
        Sketch='My Cheeseshop Sketch',
    )


def cheeseshop(kind, *args, **kwargs):
    print('-- Do you have any', kind, '?')
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print('-' * 40)
    for kw in kwargs:
        print(kw, ':', kwargs[kw])
    
    
if __name__ == "__main__":
    main()