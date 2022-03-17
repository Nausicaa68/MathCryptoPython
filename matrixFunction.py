import math


def calculate_a_determinant(matrix):

    if(math.sqrt(len(matrix)) == 2):
        return ((matrix[0]*matrix[3]) - (matrix[1]*matrix[2]))
    elif(math.sqrt(len(matrix)) == 3):
        return ((matrix[0]*matrix[4]*matrix[8]) + (matrix[1]*matrix[5]*matrix[6]) + (matrix[2]*matrix[3]*matrix[7]) - (matrix[6]*matrix[4]*matrix[2]) - (matrix[7]*matrix[5]*matrix[0]) - (matrix[8]*matrix[3]*matrix[1]))
    else:
        print("Problem to calculate the determinant")
        return 0


def invert_matrix_22(matrix):
    newMatrix = [0, 0, 0, 0]
    newMatrix[0] = matrix[3]
    newMatrix[1] = -(matrix[1])
    newMatrix[2] = -(matrix[2])
    newMatrix[3] = matrix[0]

    return newMatrix


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


def ask_for_matrix(nbValue):
    matrix = []

    for i in range(nbValue):
        value = int(input("Value " + str(i) + " : "))
        matrix.append(value)

    return matrix


if __name__ == "__main__":

    Amat = [2, 7, 21, 20]
    Bmat = [12, 20]
    mat2 = [1, 2]

    print(add_matrix_2_and_2(Bmat, mat2))  # waiting : [13,22]
    print(add_matrix_2_and_2(mat2, Bmat))  # waiting : [13,22]

    print(mult_matrix_4_time_2(Amat, Bmat))  # waiting : [164,652]
    print(mult_matrix_with_a_number(Amat, 2))  # waiting : [4,14,42,40]

    mat = [2, 11, 7, 8]
    print(calculate_a_determinant(mat))  # waiting : -61
    print(invert_matrix_22(mat))  # waiting : [8,-11,-7,2]
    
