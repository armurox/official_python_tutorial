#!/usr/bin/env python3
from point import Point

def main():
    show_point((1, 2))
    show_point((0, 0))
    try:
        show_point(1)
    except ValueError as e:
        print(e.args[0])
    print(match_with_or(401))
    show_point_with_classes(Point(1, 2))
    show_point_with_classes(Point(0, 2))
    show_point_with_classes(Point(4, 0))
    show_point_with_classes(Point(0, 0))


def match_with_or(example: int) -> str | None:
    match example:
        case 401 | 403 | 404:
            return "None allowed"
        case _:
            return None


def show_point(point: tuple) -> None:
    match point:
        case (0, 0):
            print('Origin')
        case (0, y):
            print(f'Y={y}')
        case (x, 0):
            print(f'X={x}')
        case (x, y):
            print(f'X={x}. Y={y}')
        case _:
            raise ValueError('Not a point')


def show_point_with_classes(point: Point) -> None:
    match point:
        case Point(0, 0):  # works because of __match_args__ in the Point class definition
            print('Origin')
        case Point(x=0, y=y):
            print(f'Y={y}')
        case Point(x, 0):
            print(f'X={x}')
        case Point(x=x, y=y):
            print(f'X={x}. Y={y}')
        case _:
            raise ValueError('Not a point')


if __name__ == "__main__":
    main()
