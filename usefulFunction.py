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
    deterInARing = bring_a_number_in_a_ring(calculate_a_determinant(matrix), n)
    gcd = math.gcd(calculate_a_determinant(matrix), n)
    print(deterInARing, " gcd ", n, " = ", gcd)
    if(gcd == 1):
        print("la matrice est invertible")
        return True
    else:
        print("la matrice n'est pas invertible")
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
    deter = bring_a_number_in_a_ring(calculate_a_determinant(Amat), n)
    invertA = invert_matrix_22(Amat)
    invertAInARing = invert_matrix_in_a_ring(Amat, n)
    deterInvert = invert_a_number_in_a_ring(deter, n)

    print("Inv de A :\n", Amat, "(-1) = ", deter, "(-1) * ", invertA,
          " = ", deterInvert, "*", invertAInARing, " = ", end="")

    newMat = mult_matrix_with_a_number(invertAInARing, deterInvert)

    print(" = ", newMat)

    for i in range(len(newMat)):
        newMat[i] = bring_a_number_in_a_ring(newMat[i], n)

    print(" = ", newMat)

    return newMat


def new_B_matrix(newAmat, Bmat, n):
    newMat = mult_matrix_4_time_2(newAmat, Bmat)

    print("Inv de B :\n", Bmat, "(-1) =  -1 * ",
          newAmat, " * ", Bmat, " = -", newMat, end="")

    newMat = mult_matrix_with_a_number(newMat, -1)

    print(" = ", newMat, end="")

    for i in range(len(newMat)):
        newMat[i] = bring_a_number_in_a_ring(newMat[i], n)

    print(" = ", newMat)

    return newMat


"""
def decipher(text, Amatrix, Bmatrix, n):
    decipher_text = ""
    text = text.lower()

    print("Deciphering : ", text, "\n")

    for i in range(0, len(text), 2):
        cypherMat = [ord(text[i]) - 97, ord(text[i+1]) - 97]

        print(cypherMat, end="")

        res = mult_matrix_4_time_2(Amatrix, cypherMat)
        res = add_matrix_2_and_2(res, Bmatrix)

        for i in range(len(res)):
            res[i] = bring_a_number_in_a_ring(res[i], n)
            decipher_text += chr(res[i]+97)

        print(" -> ", res)

    return decipher_text
"""


def transform_a_text_in_number(text):
    textMat = []
    text = text.lower()
    for i in range(len(text)):
        textMat.append((ord(text[i]) - 97))

    print(text, " = ", textMat)

    return textMat


def transform_numbers_in_a_text(textMat):
    text = ""

    for i in range(len(textMat)):
        text += ((chr(textMat[i] + 97)))

    print(textMat, " = ", text)

    return text


def decipher_with_number(text, Amatrix, Bmatrix, n):
    decipher_text = []

    print("Deciphering : ", text, "\n")

    for i in range(0, len(text), 2):
        cypherMat = [text[i], text[i+1]]

        print(cypherMat, end="")

        res = mult_matrix_4_time_2(Amatrix, cypherMat)
        res = add_matrix_2_and_2(res, Bmatrix)

        for i in range(len(res)):
            res[i] = bring_a_number_in_a_ring(res[i], n)
            decipher_text.append(res[i])

        print(" -> ", res)

    return decipher_text


def main_deciphering_vigenere(Amat, Bmat, n, text):
    determinant = calculate_a_determinant(Amat)
    print("Determinant de A : ", determinant, end="")
    determinantInN = bring_a_number_in_a_ring(determinant, n)
    print(" =  ", determinantInN)

    isInvertible = is_invertible_in_n(Amat, n)
    print(" ")

    if(isInvertible):
        newAmat = new_A_matrix(Amat, n)
        print(" ")
        newBmat = new_B_matrix(newAmat, Bmat, n)
        print(" ")

        decrypt = decipher_with_number(text, newAmat, newBmat, n)
        print(decrypt)

        return decrypt

    else:
        return 0


def ciphering_cesar(keyA, keyB, n, text):
    text = text.lower()
    encipher_text = ""

    for i in range(len(text)):
        print(text[i], " = ", (ord(text[i]) - 97), end="")
        result = keyA * (ord(text[i]) - 97) + keyB
        print(" = ", result, end="")
        result = bring_a_number_in_a_ring(result, n)
        print(" = ", result, " = ", (chr(result + 97)),  end="")
        encipher_text += chr(result + 97)
        print("")

    print(encipher_text)

    return encipher_text


def calc_deciphering_key_cesar(keyA, keyB, n):
    decipherKeyA = invert_a_number_in_a_ring(keyA, n)
    decipherKeyB = decipherKeyA*keyB*(-1)
    decipherKeyB = bring_a_number_in_a_ring(decipherKeyB, n)

    return decipherKeyA, decipherKeyB


if __name__ == "__main__":

    # print(invert_a_number_in_a_ring(63, 10))  # waiting : 7
    # mat = [2, 11, 7, 8]
    # print(calculate_a_determinant(mat))  # waiting : -61
    # print(bring_a_number_in_a_ring(-214, 28))  # waiting : 10
    # print(invert_matrix_22(mat))  # waiting : [8,-11,-7,2]
    # print(invert_matrix_in_a_ring(mat, 26))  # waiting : [8,15,19,2]

    # Amat = [2, 7, 21, 20]
    # Bmat = [12, 20]
    # mat2 = [1, 2]

    # print(add_matrix_2_and_2(Bmat, mat2))  # waiting : [13,22]
    # print(add_matrix_2_and_2(mat2, Bmat))  # waiting : [13,22]

    # print(mult_matrix_4_time_2(Amat, Bmat))  # waiting : [164,652]
    # print(mult_matrix_with_a_number(Amat, 2))  # waiting : [4,14,42,40]

    # N = 26
    # Amat = [2, 11, 7, 8]
    # Bmat = [12, 20]

    # newAmat = new_A_matrix(Amat, N)
    # newBmat = new_B_matrix(newAmat, Bmat, N)
    # print(newAmat)  # waiting : [2,7,21,20]
    # print(newBmat)  # waiting : [18,24]

    # print(decipher("mivmaz", newAmat, newBmat, N))  # waiting : uuodle

    # matTest1 = [2, 13, 10, 12]
    # print(is_invertible_in_n(matTest1, 15))  # waiting : true
    # matTest1 = [8, 17, 14, 3]
    # print(is_invertible_in_n(matTest1, 28))  # waiting : false
    # matTest1 = [3, 0, 9, 0, 1, 6, 4, 3, 1]
    # print(is_invertible_in_n(matTest1, 12))  # waiting : false
    # matTest1 = [0, 7, 2, 3, 4, 0, 8, 0, 2]
    # print(is_invertible_in_n(matTest1, 9))  # waiting : true

    N = 26
    Amat = [2, 11, 7, 8]
    Bmat = [12, 20]

    # main_deciphering_vigenere(Amat, Bmat, N, "mivmaz")

    ciphering_cesar(5, 3, 11, "decide")
    ciphering_cesar(9, 6, 11, "bggkcdcb")

    print(calc_deciphering_key_cesar(15, 20, 28))

    cipher_text = transform_a_text_in_number("mivmaz")
    print(cipher_text)

    decipher_text = main_deciphering_vigenere(Amat, Bmat, N, cipher_text)

    print(decipher_text)

    print(transform_numbers_in_a_text(decipher_text))
