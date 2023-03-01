file_decode = open("decode.txt", "r")
file_hardB = open("hardB.txt", "a")

file_hardB.write(file_decode.read())

file_decode.close()
file_hardB.close()