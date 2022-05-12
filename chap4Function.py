"""
Functions of the chapter 4

Based on the Mathematics for Cryptography class - Efrei Paris
Course from Nicolas Flasque & Federico Zalamea

Author of the program : Nausicaä

"""

import math
from chap1Function import find_all_invert_in_a_ring
from chap3Function import totient
from matrixFunction import ask_for_matrix
from chap1Function import bring_a_number_in_a_ring
from chap1Function import invert_a_number_in_a_ring
from chap3Function import pow_mod
import chap1Function as ch1f


"""
To-do list : 
find all divisors of a number ex : 10 -> 1 2 5 10
find inverses and order of all the element of a group
-> when a^x % n = 1
find generators (when ord(g) = |G|)

"""


def main_chap4():
    """
        Main of the chapter 4
        Propose : 
            1 - encipher in Elgamal
            2 - decipher in Elgamal
            3 - calculate the order of a number
            4 - calculate the list of the generator
    """

    choice = 0
    while(choice != 99):

        print("What do you want to do : \n")
        print("1 - encipher in Elgamal")
        print("2 - decipher in Elgamal")
        print("3 - calculate the order of a number")
        print("4 - calculate the list of the generator")

        print("\n99 - Quit\n")

        choice = int(input("Choice : "))

        if(choice == 1):
            print("Public domain : ")
            N = int(input("N : "))
            g = int(input("generator : "))

            print("Information : ")
            e = int(input("e of the receiver :"))
            k = int(input("k chosen : "))

            print("Message : ")
            numberOfValues = int(input("Number of values in the message : "))
            mess = ask_for_matrix(numberOfValues)
            print("\n")

            print("Result = ", cipher_in_Elgamal(mess, g, e, k, N, 3, 1))

        elif(choice == 2):
            print("Public domain : ")
            N = int(input("N : "))

            print("Information : ")
            d = int(input("d of the receiver :"))
            r = int(input("r of the message : "))

            print("Message : ")
            numberOfValues = int(input("Number of values in the message : "))
            mess = ask_for_matrix(numberOfValues)
            print("\n")

            print("Result = ", decipher_in_Elgamal(mess, r, d, N, 3, 1))

        elif(choice == 3):
            number = int(input("Number to test : "))
            N = int(input("N : "))
            idel = int(input("identity element of the group : "))
            print("\n")

            print("Result = ", calc_order_of_a_number(number, N, idel, 1))

        elif(choice == 4):
            N = int(input("N : "))
            print("\n")

            print("Result = ", calc_generator(N, 1))

        elif(choice == 99):
            print("Bye")

        else:
            print("Error")

        print("\n\n")


def exo27(list, N):

    print(" *  ", end="")
    for number in list:
        print(number, "   ", end="")
    print()

    for number in list:
        print(number, "  ", end="")
        for number2 in list:
            print((number * number2) % N, "   ", end="")
        print()

    print("\n\n")


def calculate_Elgamal_key(g, d, N, show=0):
    e = pow_mod(g, d, N)

    if(show != 0):
        print("e = g^d [N] = ", g, "^", d, "[", N, "] = ", e)

    return e


def operation(x, y, op):
    """
    OP : 
        1 - addition
        2 - soustraction
        3 - multiplication
        4 - division
        5 - puissance x^y
        6 - particular
    """

    if(op == 1):
        return x + y
    elif(op == 2):
        return x - y
    elif(op == 3):
        return x*y
    elif(op == 4):
        return x/y
    elif(op == 5):
        return pow(x, y)
    elif(op == 6):
        return -1
    else:
        print("ERROR in operation")
        return -99


def cipher_in_Elgamal(text, g, e, k, N, ope, show=0):

    r = pow_mod(g, k, N)
    if(show != 0):
        print("r = g^k [N] = ", g, "^", k, "[", N, "] = ", r)

    cipher_text = []

    for each in text:
        ek = pow_mod(e, k, N)
        y = operation(each, ek, ope)
        ymodN = bring_a_number_in_a_ring(y, N)

        cipher_text.append(ymodN)

        if(show != 0):
            print("y = ", each, "∆", "(", e, " ^ ", k,
                  ") [", N, "] = ", y, "[", N, "] = ", ymodN)

    return r, cipher_text


def decipher_in_Elgamal(text, r, d, N, ope, show=0):

    decipher_text = []

    for each in text:
        rd = pow_mod(r, d, N)
        rd1 = invert_a_number_in_a_ring(rd, N)

        x = operation(each, rd1, ope)
        xmodN = bring_a_number_in_a_ring(x, N)

        decipher_text.append(xmodN)

        if(show != 0):
            print("x = ", each, "∆", "(", r, " ^ ", d, ")(-1)",
                  "[", N, "] = ", each, "∆", rd1, " = ", x, "[", N, "] = ", xmodN)

    return decipher_text


def find_private_key(g, e, N, show=0):
    print("\nFind d :")
    for i in range(N):
        d = pow_mod(g, i, N)

        if(show != 0):
            print(g, "^", i, "[", N, "] = ", d)

        if(d == e):
            print("so d = ", i, "\n")
            return i

    print("All values were passed. Error.\n")
    return -1


def exo43_44():

    # exo43
    N = 23
    g = 7
    ea = 13
    da = 10
    eb = 15

    calculate_Elgamal_key(g, da, N, 1)  # waiting : 13
    cipher_in_Elgamal([12], g, eb, 7, N, 3, 1)  # waiting : r = 5  y = 17
    decipher_in_Elgamal([11], 20, da, N, 3, 1)  # waiting : 10
    find_private_key(g, eb, N, 1)  # waiting : 9

    # exo44
    N = 23
    g = 10
    ea = 17
    da = 17
    eb = 13

    calculate_Elgamal_key(g, da, N, 1)
    cipher_in_Elgamal([11], g, eb, 47, N, 3, 1)
    decipher_in_Elgamal([3], 3, da, N, 3, 1)
    find_private_key(g, eb, N, 1)


def find_all_divisors(number):
    allDivisors = []
    for i in range(1, number+1):
        if number % i == 0:
            allDivisors.append(i)

    return allDivisors


def calc_order_of_a_number(number, N, identityElement, show=0):

    phi = totient(N, show)
    allDiv = find_all_divisors(phi)
    if(show != 0):
        print("divisor of", phi, "=", allDiv)

    for div in allDiv:
        power = pow_mod(number, div, N)
        if(show != 0):
            print(number, "^", div, " = ", power)

        if(power == identityElement):
            return div


def calc_generator(N, show=0):

    generators = []
    phi = totient(N, show)
    invert = find_all_invert_in_a_ring(N)[1]

    for inv in invert:
        order = calc_order_of_a_number(inv, N, 1)
        if(order == phi):
            generators.append(inv)

    return generators


if __name__ == "__main__":

    print("Chap4")
    # exo27([3, 7, 8, 12, 13], 17)
    # exo27([1, 4, 13, 16], 17)
    # exo27([1, 5, 7, 10, 12], 17)

    # calculate_Elgamal_key(7, 10, 23, 1)  # waiting : 13
    # cipher_in_Elgamal([12], 7, 15, 7, 23, 3, 1)  # waiting : r = 5  y = 17
    # decipher_in_Elgamal([11], 20, 10, 23, 3, 1)  # waiting : 10
    # find_private_key(7, 15, 23, 1)  # waiting : 9

    # print(calc_order_of_a_number(17, 40, 1, 1))  # waiting : 4
    #print(calc_generator(50, 1))

    main_chap4()
