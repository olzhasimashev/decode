from math import sin, sqrt, pow

x = int(input())
y = int(input())

print((sqrt(sin(x)+pow(y, 3))+sqrt(x+y))/(2*x+y))