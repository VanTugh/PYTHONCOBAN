import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def distance(self , point):
        return math.hypot(point.x - self.x , point.y - self.y)
class Circle:
    def __init__(self, center, radius):
        self.center = Point(center.x, center.y)
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def Perimeter(self):
        return 2 * math.pi * self.radius
    def testBelong(self, point):
        distance = self.center.distance(point)
        return distance <= self.radius
def main():
    center = Point(1, 1)
    circle = Circle(center, 5)

    print(f"Circle Center: {circle.center}")
    print(f"Circle Radius: {circle.radius}")
    print(f"Circle Area: {circle.area()}")
    print(f"Circle Perimeter: {circle.Perimeter()}")

    test_point_inside = Point(3, 4)
    test_point_outside = Point(6, 8)

    print(f"Point {test_point_inside} inside circle: {circle.testBelong(test_point_inside)}")
    print(f"Point {test_point_outside} inside circle: {circle.testBelong(test_point_outside)}")
if __name__ == "__main__":
    main()