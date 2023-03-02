class Rect:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def isSquare(self):
        if object.lenght == object.width:
            return True
        else:
            return False
        
lenght = int(input())
width = int(input())

object = Rect(lenght, width)

print(object.isSquare())