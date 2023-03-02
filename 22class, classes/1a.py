class Point:
    def __init__(self, x = 5, y = 10):
        self.x = x
        self.y = y

object = Point()

input = input()

if input == "x":
    print(object.x)
elif input == "y":
    print(object.y)