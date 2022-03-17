import math
from matrixFunction import *


def invert_a_number_in_a_ring(number, n, s=1, t=0, N=0):
    return (n < 2 and t % N or invert_a_number_in_a_ring(n, number % n, t, s-number//n*t, N or n), -1)[n < 1]


def bring_a_number_in_a_ring(number, n):
    return number % n


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


def invert_matrix_in_a_ring(matrix, n):
    invertMatrix = invert_matrix_22(matrix)
    for i in range(len(invertMatrix)):
        invertMatrix[i] = bring_a_number_in_a_ring(invertMatrix[i], n)

    return invertMatrix


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

    print(" = ", newMat)

    for i in range(len(newMat)):
        newMat[i] = bring_a_number_in_a_ring(newMat[i], n)

    print(" = ", newMat)

    return newMat


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


def decipher(text, Amatrix, Bmatrix, n):
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

        decrypt = decipher(text, newAmat, newBmat, n)
        print(decrypt)

        return decrypt

    else:
        return 0


def ciphering_cesar(keyA, keyB, n, textMat):
    encipher_text = []

    for i in range(len(textMat)):
        result = keyA * textMat[i] + keyB
        print(textMat[i], " = ", result, end="")
        result = bring_a_number_in_a_ring(result, n)
        print(" = ", result)
        encipher_text.append(result)

    print(encipher_text)

    return encipher_text


def calc_deciphering_key_cesar(keyA, keyB, n):
    decipherKeyA = invert_a_number_in_a_ring(keyA, n)
    print(keyA, " -> ", decipherKeyA)
    decipherKeyB = decipherKeyA*keyB*(-1)
    print(keyB, " -> ", decipherKeyB, " -> ", end="")
    decipherKeyB = bring_a_number_in_a_ring(decipherKeyB, n)
    print(decipherKeyB)

    return decipherKeyA, decipherKeyB


def main_chap2():

    choice = 0
    while(choice != 99):

        print("What do you want to do : ")
        print(" - ")
        print("1 - Determinant")
        print("2 - Matrice Invertible ?")
        print("3 - Viginere with text")
        print("4 - Viginere with numbers")
        print("5 - Encipher in Cesar")
        print("6 - decipher in Cesar with text")
        print("7 - decipher in Cesar with number")

        print("99 - Quit")

        choice = int(input("Choice : "))

        if(choice == 1 or choice == 2):
            ring = int(input("Ring : "))
            numberOfValueInMatrix = int(
                input("Number of values in the matrix : "))
            mat = ask_for_matrix(numberOfValueInMatrix)
            deter = calculate_a_determinant(mat)
            print("Determinant de ", mat, " = ", deter, " = ",
                  bring_a_number_in_a_ring(deter, ring))

            if(choice == 2):
                is_invertible_in_n(mat, ring)

        elif(choice == 3):
            ring = int(input("Ring : "))

            print("Matrice A : ")
            Amat = ask_for_matrix(4)
            print("Matrice B : ")
            Bmat = ask_for_matrix(2)

            text = input("Text : ")

            print("\n")
            textMat = transform_a_text_in_number(text)
            dec = main_deciphering_vigenere(Amat, Bmat, ring, textMat)
            transform_numbers_in_a_text(dec)

        elif(choice == 4):
            ring = int(input("Ring : "))

            print("Matrice A : ")
            Amat = ask_for_matrix(4)
            print("Matrice B : ")
            Bmat = ask_for_matrix(2)

            numberOfValueInMatrix = int(
                input("Number of values in the cipher matrix : "))
            text = ask_for_matrix(numberOfValueInMatrix)

            print("\n")
            main_deciphering_vigenere(Amat, Bmat, ring, text)

        elif(choice == 5):
            ring = int(input("Ring : "))
            keyA = int(input("key A : "))
            keyB = int(input("key B : "))
            text = input("Text : ")

            print("\n")
            textMat = transform_a_text_in_number(text)
            enc = ciphering_cesar(keyA, keyB, ring, textMat)
            transform_numbers_in_a_text(enc)

        elif(choice == 6):
            ring = int(input("Ring : "))
            keyA = int(input("key A : "))
            keyB = int(input("key B : "))
            text = input("Text : ")

            print("\n")
            decKey = calc_deciphering_key_cesar(keyA, keyB, ring)
            decKeyA = decKey[0]
            decKeyB = decKey[1]

            print("\n")
            textMat = transform_a_text_in_number(text)
            dec = ciphering_cesar(decKeyA, decKeyB, ring, textMat)
            transform_numbers_in_a_text(dec)

        elif(choice == 7):
            ring = int(input("Ring : "))
            keyA = int(input("key A : "))
            keyB = int(input("key B : "))

            numberOfValueInMatrix = int(
                input("Number of values in the cipher matrix : "))
            text = ask_for_matrix(numberOfValueInMatrix)

            print("\n")
            decKey = calc_deciphering_key_cesar(keyA, keyB, ring)
            decKeyA = decKey[0]
            decKeyB = decKey[1]

            print("\n")
            ciphering_cesar(decKeyA, decKeyB, ring, text)

        elif(choice == 99):
            print("Bye")

        else:
            print("Error")

        print("\n\n")


if __name__ == "__main__":

    N = 26
    Amat = [2, 11, 7, 8]
    Bmat = [12, 20]

    print(invert_a_number_in_a_ring(63, 10))  # waiting : 7
    print(invert_matrix_in_a_ring(Amat, 26))  # waiting : [8,15,19,2]

    newAmat = new_A_matrix(Amat, N)
    newBmat = new_B_matrix(newAmat, Bmat, N)
    print(newAmat)  # waiting : [2,7,21,20]
    print(newBmat)  # waiting : [18,24]

    # matTest1 = [2, 13, 10, 12]
    # print(is_invertible_in_n(matTest1, 15))  # waiting : true
    # matTest1 = [8, 17, 14, 3]
    # print(is_invertible_in_n(matTest1, 28))  # waiting : false
    # matTest1 = [3, 0, 9, 0, 1, 6, 4, 3, 1]
    # print(is_invertible_in_n(matTest1, 12))  # waiting : false
    # matTest1 = [0, 7, 2, 3, 4, 0, 8, 0, 2]
    # print(is_invertible_in_n(matTest1, 9))  # waiting : true

    # main_deciphering_vigenere(Amat, Bmat, N, "mivmaz")

    # ciphering_cesar(5, 3, 11, "decide")
    # ciphering_cesar(9, 6, 11, "bggkcdcb")

    # print(calc_deciphering_key_cesar(15, 20, 28))

    # cipher_text = transform_a_text_in_number("mivmaz")
    # print(cipher_text)

    # decipher_text = main_deciphering_vigenere(Amat, Bmat, N, cipher_text)

    # print(decipher_text)

    # print(transform_numbers_in_a_text(decipher_text))
