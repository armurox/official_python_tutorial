class Point:
    __match_args__ = ('x', 'y')  # so that keyword arguments are not enforced
    def __init__(self, x, y):
        self.x = x
        self.y = y