class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        return pow((pow(self.x - other.x, 2) + pow(self.y - other.y, 2)), 0.5)