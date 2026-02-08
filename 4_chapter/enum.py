#!/usr/bin/env python3
from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


def main():
    while True:
        try:
            color = Color(input('Enter your choice of red, green or blue: '))
            break
        except ValueError as e:
            print(e.args[0])
        

    decide_what_to_do_with(color)


def decide_what_to_do_with(color):
    match color:
        case Color.RED:
            print('I see red!')
        case Color.GREEN:
            print('Grass is green')
        case Color.BLUE:
            print("I'm feeling the blues:(")
    
    
    
if __name__ == "__main__":
    main()
