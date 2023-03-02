class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, object):
        return ((object.x-self.x)**2+(object.y-self.y)**2)**0.5

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

object1 = Point(x1, y1)
object2 = Point(x2, y2)

print(object1.dist(object2))