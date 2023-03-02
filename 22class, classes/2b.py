class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getPerimeter(self):
        return 2*(object.length+object.width)
    
    def getArea(self):
        return object.length*object.width
    
    def getDiagonal(self):
        return round((object.length**2+object.width**2)**0.5, 2)
    
length = int(input())
width = int(input())

object = Rect(length, width)

print(object.getPerimeter(), object.getArea(), object.getDiagonal())