import os

file_decode = open("decode.txt", "a")
file_hardB = open("hardB.txt", "r")

file_decode.write(file_hardB.read())

file_decode.close()
file_hardB.close()

os.remove("hardB.txt")