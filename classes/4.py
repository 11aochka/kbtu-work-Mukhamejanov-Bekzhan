import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        """Displays the coordinates of the point."""
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        """Moves the point to new coordinates."""
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        """Computes the Euclidean distance between two points."""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)