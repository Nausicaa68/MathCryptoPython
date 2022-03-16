import math

sizeOfTheMatrix = int(input("Size of the matrix : "))
matrix = []
for i in range(sizeOfTheMatrix*sizeOfTheMatrix):
    value = int(input("Value " + str(i) + " : "))
    matrix.append(value)

print(matrix)


