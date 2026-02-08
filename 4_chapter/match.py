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
    show_multiple_points_with_classes([Point(0, 1), Point(0, 2)])
    show_multiple_points_with_classes([Point(0, 0), Point(0, 0)])
    show_multiple_points_with_classes([Point(1, 1)])
    show_multiple_points_with_classes([Point(0, 0)])
    show_multiple_points_with_classes([Point(1, 4), Point(4,2), Point(6,3), Point(7,4), (8,5)])
    show_multiple_points_with_classes({'bandwidth': 2, "latency": 3, "hello_world": 'yay'})


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


def show_multiple_points_with_classes(points):
    match points:
        case []:
            print('No points')
        case [Point(0, 0)]:
            print('The origin')
        case [Point(x, y)] if x == y:  # guard - value capture happens before the guard is evaluated
            print(f'Y=X at {x}')
        case [Point(x, y)]:
            print(f'Single point {x}, {y}')
        case [Point(0, 0), Point(0, 0)]:
            print('Two at the origin')
        case [Point(0, y1), Point(0, y2)]:
            print(f'Two on the Y axis at {y1}, {y2}')
        case [Point(x1, y1), Point(x2, y2) as p2, *rest]:  # as and unpacking
            print(f'X1={x1}, Y1={y1}, X2={p2.x}, Y2={p2.y}, rest is {rest}')
        case {'bandwidth': b, "latency": l, **rest}:  # dictionary match example
            print(f'bandwidth={b}, latency={l}, rest is {rest}')
        case _:
            print('Something else')



if __name__ == "__main__":
    main()
