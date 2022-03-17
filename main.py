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
    print("3 - Viginere with text")
    print("4 - Viginere with numbers")
    print("5 - Encipher in Cesar")
    print("6 - decipher in Cesar with text")
    print("7 - decipher in Cesar with number")

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
