from usefulFunction import *


def ask_for_matrix(nbValue):
    matrix = []

    for i in range(nbValue):
        value = int(input("Value " + str(i) + " : "))
        matrix.append(value)

    return matrix


choice = 0
while(choice != 99):

    print("What do you want to do : ")
    print(" - ")
    print("1 - Determinant")
    print("2 - Matrice Invertible ?")
    print("3 - Viginere")
    print("4 - Viginere with numbers")
    print("5 - Encipher in Cesar")
    print("6 - decipher in Cesar")

    print("99 - Quit")

    choice = int(input("Choice : "))

    if(choice == 1 or choice == 2):
        ring = int(input("Ring : "))
        numberOfValueInMatrix = int(input("Number of values in the matrix : "))
        mat = ask_for_matrix(numberOfValueInMatrix)
        deter = calculate_a_determinant(mat)
        print("Determinant de ", mat, " = ", deter, " = ",
              bring_a_number_in_a_ring(deter, ring))

        if(choice == 2):
            is_invertible_in_n(mat, ring)

    if(choice == 3):
        ring = int(input("Ring : "))

        print("Matrice A : ")
        Amat = ask_for_matrix(4)
        print("Matrice B : ")
        Bmat = ask_for_matrix(2)

        text = input("Text : ")

        print("\n")
        main_deciphering_vigenere(Amat, Bmat, ring, text)

    if(choice == 4):
        ring = int(input("Ring : "))

        print("Matrice A : ")
        Amat = ask_for_matrix(4)
        print("Matrice B : ")
        Bmat = ask_for_matrix(2)

        numberOfValueInMatrix = int(input("Number of values in the cipher matrix : "))
        text = ask_for_matrix(numberOfValueInMatrix)

        print("\n")
        main_deciphering_vigenere(Amat, Bmat, ring, text)

    if(choice == 5):
        ring = int(input("Ring : "))
        keyA = int(input("key A : "))
        keyB = int(input("key B : "))
        text = input("Text : ")

        ciphering_cesar(keyA, keyB, ring, text)

    if(choice == 6):
        ring = int(input("Ring : "))
        keyA = int(input("key A : "))
        keyB = int(input("key B : "))
        text = input("Text : ")

        decKey = calc_deciphering_key_cesar(keyA, keyB, ring)
        decKeyA = decKey[0]
        decKeyB = decKey[1]

        ciphering_cesar(decKeyA, decKeyB, ring, text)

    if(choice == 99):
        print("Bye")

    else:
        print("Error")

    print("\n\n")
