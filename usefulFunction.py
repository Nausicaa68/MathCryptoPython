import math


def invert_a_number_in_a_ring(number, n, s=1, t=0, N=0):
    return (n < 2 and t % N or invert_a_number_in_a_ring(n, number % n, t, s-number//n*t, N or n), -1)[n < 1]


def bring_a_number_in_a_ring(number, n):
    return number % n


def calculate_a_determinant(matrix):

    if(math.sqrt(len(matrix)) == 2):
        return ((matrix[0]*matrix[3]) - (matrix[1]*matrix[2]))
    elif(math.sqrt(len(matrix)) == 3):
        return ((matrix[0]*matrix[4]*matrix[8]) + (matrix[1]*matrix[5]*matrix[6]) + (matrix[2]*matrix[3]*matrix[7]) - (matrix[6]*matrix[4]*matrix[2]) - (matrix[7]*matrix[5]*matrix[0]) - (matrix[8]*matrix[3]*matrix[1]))
    else:
        print("Problem to calculate the determinant")
        return 0


def is_invertible_in_n(matrix, n):
    if(math.gcd(calculate_a_determinant(matrix), n) == 1):
        return True
    else:
        return False


def invert_matrix_22(matrix):
    newMatrix = [0, 0, 0, 0]
    newMatrix[0] = matrix[3]
    newMatrix[1] = -(matrix[1])
    newMatrix[2] = -(matrix[2])
    newMatrix[3] = matrix[0]

    return newMatrix


def invert_matrix_in_a_ring(matrix, n):
    invertMatrix = invert_matrix_22(matrix)
    for i in range(len(invertMatrix)):
        invertMatrix[i] = bring_a_number_in_a_ring(invertMatrix[i], n)

    return invertMatrix


def mult_matrix_4_time_2(mat4, mat2):
    result = [0, 0]
    result[0] = mat4[0]*mat2[0] + mat4[1]*mat2[1]
    result[1] = mat4[2]*mat2[0] + mat4[3]*mat2[1]

    return result


def mult_matrix_with_a_number(mat, number):
    for i in range(len(mat)):
        mat[i] = number*mat[i]
    return mat


def add_matrix_2_and_2(mat1, mat2):
    return [(mat1[0] + mat2[0]), (mat1[1] + mat2[1])]


def new_A_matrix(Amat, n):
    deter = calculate_a_determinant(Amat)
    invertA = invert_matrix_in_a_ring(Amat, n)
    deterInvert = invert_a_number_in_a_ring(deter, n)
    newMat = mult_matrix_with_a_number(invertA, deterInvert)

    for i in range(len(newMat)):
        newMat[i] = bring_a_number_in_a_ring(newMat[i], n)

    return newMat


def new_B_matrix(newAmat, Bmat, n):
    newMat = mult_matrix_4_time_2(newAmat, Bmat)
    newMat = mult_matrix_with_a_number(newMat, -1)

    for i in range(len(newMat)):
        newMat[i] = bring_a_number_in_a_ring(newMat[i], n)

    return newMat


def decipher(text, Amatrix, Bmatrix, n):
    decipher_text = ""
    text = text.lower()

    for i in range(0, len(text), 2):
        cypherMat = [ord(text[i]) - 97, ord(text[i+1]) - 97]
        res = mult_matrix_4_time_2(Amatrix, cypherMat)
        res = add_matrix_2_and_2(res, Bmatrix)

        for i in range(len(res)):
            res[i] = bring_a_number_in_a_ring(res[i], n)
            decipher_text += chr(res[i]+97)
            print(res)

    return decipher_text


print(invert_a_number_in_a_ring(63, 10))  # waiting : 7
mat = [2, 11, 7, 8]
print(calculate_a_determinant(mat))  # waiting : -61
print(bring_a_number_in_a_ring(-214, 28))  # waiting : 10
print(invert_matrix_22(mat))  # waiting : [8,-11,-7,2]
print(invert_matrix_in_a_ring(mat, 26))  # waiting : [8,15,19,2]

Amat = [2, 7, 21, 20]
Bmat = [12, 20]
mat2 = [1, 2]

print(add_matrix_2_and_2(Bmat, mat2))  # waiting : [13,22]
print(add_matrix_2_and_2(mat2, Bmat))  # waiting : [13,22]

print(mult_matrix_4_time_2(Amat, Bmat))  # waiting : [164,652]
print(mult_matrix_with_a_number(Amat, 2))  # waiting : [4,14,42,40]


N = 26
Amat = [2, 11, 7, 8]
Bmat = [12, 20]

newAmat = new_A_matrix(Amat, N)
newBmat = new_B_matrix(newAmat, Bmat, N)
print(newAmat)  # waiting : [2,7,21,20]
print(newBmat)  # waiting : [18,24]

print(decipher("mivmaz", newAmat, newBmat, N))  # waiting : uuodle


matTest1 = [2, 13, 10, 12]
print(is_invertible_in_n(matTest1, 15))  # waiting : true
matTest1 = [8, 17, 14, 3]
print(is_invertible_in_n(matTest1, 28))  # waiting : false
matTest1 = [3, 0, 9, 0, 1, 6, 4, 3, 1]
print(is_invertible_in_n(matTest1, 12))  # waiting : false
matTest1 = [0, 7, 2, 3, 4, 0, 8, 0, 2]
print(is_invertible_in_n(matTest1, 9))  # waiting : true
