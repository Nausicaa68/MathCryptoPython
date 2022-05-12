"""
Functions of the chapter 3

Based on the Mathematics for Cryptography class - Efrei Paris
Course from Nicolas Flasque & Federico Zalamea

Author of the program : Nausicaä

"""

from chap1Function import *
from matrixFunction import ask_for_matrix


def pow_mod(x, y, modulo):
    """
    x^y [modulo]
    """

    if y == 0:
        return 1
    elif y == 1:
        return x % modulo
    else:
        root = pow_mod(x, y // 2, modulo)
        if y % 2 == 0:
            return (root * root) % modulo
        else:
            return (root * root * x) % modulo


def totient(n, show=0):
    """
    Compute the euler totient with find_all_invert_in_a_ring
    Brute force algorithm
    """

    invertibles = find_all_invert_in_a_ring(n)[1]
    phiN = len(invertibles)
    if(show != 0):
        print("Phi(", n, ") = ", phiN)

    return phiN


def totient_faster(n, show=0):
    """
    Compute the euler totient with optimized technics
    """

    phiN = 1
    if(is_prime(n)):
        phiN = n-1
        if(show != 0):
            print(n, "is prime : Phi(", n, ") = ", n, "- 1 = ", phiN)
    else:
        allPrimeFactor = prime_factors(n)

        if(checkPairwiseCoPrime(allPrimeFactor)):
            if(show != 0):
                print("Phi(", n, ") = ", end="")
                for each in allPrimeFactor:
                    print("Phi(", each, ")", end="")
                print(" = ", end="")

            for each in allPrimeFactor:
                if(show != 0):
                    print(totient(each), " ", end="")
                phiN *= totient(each)

            if(show != 0):
                print(" = ", phiN)

        else:
            print("cheh")
            print(allPrimeFactor)

    return phiN


def calculate_RSA_key(p, q, e, show=0):
    """
    Determine a RSA key with p, q and e
    Reminder : 
        n = p*q , where p and q are two different prime numbers
        e is an invertible number in Z/phi(n)Z
        d = e(-1) in Z/phi(n)Z
    """

    if(is_prime(p) and is_prime(q)):
        n = p*q
        phiN = (p-1)*(q-1)

        if(GCD(e, phiN)):
            d = invert_a_number_in_a_ring(e, phiN)

            if(show != 0):
                print("Calculate RSA key : ")
                print("n = p * q =", p, "*", q, " = ", n)
                print("Phi (", n, ") = (", p, "- 1) * (", q, "- 1) = ", phiN)
                print("d =", e, "(-1) in Z/", phiN, "Z  = ", d)
                print()

            return [[n, e], [n, d]]

        else:
            print("e (", e, ") is not coprime with phiN (", phiN, ")")
    else:
        print("p and/or q is/are not prime number")


def calculate_d(publicKey, show=0):
    """
    Quick function to compute d in RSA
    d = e(-1) in Z/phi(n)Z
    (this function use totient_faster())
    """

    d = invert_a_number_in_a_ring(
        publicKey[1], totient_faster(publicKey[0], show))
    if(show != 0):
        print("d = ", d)
    return d


def cipher_in_RSA(text, key, show=0):
    """
    Cipher/Decipher a text in RSA
    c = x^e [n] 
    The key is under the format : [n, e]
    """

    change_text = []
    for each in text:
        c = pow_mod(each, key[1], key[0])
        change_text.append(c)

        if(show != 0):
            print("c =", each, "^",
                  key[1], "[", key[0], "] = ", c)

    return change_text


def is_RSA_key_ok(publicKey, d=0):
    """
    Check if all the condition to make a good RSA key are fulfil.
    The algo check the condition on the d only if a value is enter.
    The key is under the format : [n, e]
    """

    ok = 1

    if(is_prime(publicKey[0]) == True):
        print("The key is not ok.", publicKey[0], "is prime.")
        ok = 0
    else:
        print(publicKey[0], "is not prime.")

    phiN = totient_faster(publicKey[0], 1)
    eGcdPhinN = GCD(publicKey[1], phiN)
    print(publicKey[1], "gcd", phiN, " = ", eGcdPhinN)

    if(eGcdPhinN != 1):
        print("The key is not ok.",
              publicKey[1], "and", phiN, "are not co-prime.")
        ok = 0
    else:
        print(publicKey[1], "and", phiN, "are co-prime.")

    if(d != 0):
        verif = (publicKey[1]*d) % phiN
        print(publicKey[1], "*", d, "%", phiN, " = ", verif, end="")
        if(verif != 1):
            print(" != 1.\nThe value of d is not ok.")
            ok = 0
        else:
            print("\nThe value of d is ok.")

    elif(ok == 1):
        d = invert_a_number_in_a_ring(publicKey[1], phiN)
        print("d =", publicKey[1], "(-1) in Z/", phiN, "Z  = ", d)

    if(ok == 1):
        print("The key is ok")

    print()


def generating_authentification_signature_from_A_to_B(publicKeyA, publicKeyB, sA, dA, show=0):
    """
    A is the sender, B is the receiver
    """

    if(publicKeyA[0] < publicKeyB[0]):
        step1 = pow_mod(sA, dA, publicKeyA[0])
        step2 = pow_mod(step1, publicKeyB[1], publicKeyB[0])

        if(show != 0):
            print("step1 =", sA, "^",
                  dA, "[", publicKeyA[0], "] = ", step1)
            print("step2 =", step1, "^",
                  publicKeyB[1], "[", publicKeyB[0], "] = ", step2, "\n")

    elif(publicKeyA[0] > publicKeyB[0]):
        step1 = pow_mod(sA, publicKeyB[1], publicKeyB[0])
        step2 = pow_mod(step1, dA, publicKeyA[0])

        if(show != 0):
            print("step1 =", sA, "^",
                  publicKeyB[1], "[", publicKeyB[0], "] = ", step1)
            print("step2 =", step1, "^",
                  dA, "[", publicKeyA[0], "] = ", step2, "\n")

    return step2


def check_authentification_signature_from_A_by_B(publicKeyA, publicKeyB, yAB, dB, show=0):
    """
    A is the sender, B is the receiver
    """

    if(publicKeyA[0] < publicKeyB[0]):
        step1 = pow_mod(yAB, dB, publicKeyB[0])
        step2 = pow_mod(step1, publicKeyA[1], publicKeyA[0])

        if(show != 0):
            print("step1 =", yAB, "^",
                  dB, "[", publicKeyB[0], "] = ", step1)
            print("step2 =", step1, "^",
                  publicKeyA[1], "[", publicKeyA[0], "] = ", step2)

    elif(publicKeyA[0] > publicKeyB[0]):
        step1 = pow_mod(yAB, publicKeyA[1], publicKeyA[0])
        step2 = pow_mod(step1, dB, publicKeyB[0])

        if(show != 0):
            print("step1 =", yAB, "^",
                  publicKeyA[1], "[", publicKeyA[0], "] = ", step1)
            print("step2 =", step1, "^",
                  dB, "[", publicKeyB[0], "] = ", step2)

    return step2


def equations(power, answer, ring, show=0):
    """
    Solve an equation under the format : x^5 = 41
    """

    phi = totient_faster(ring, show)
    invert = invert_a_number_in_a_ring(power, phi)
    x = pow_mod(answer, invert, ring)

    if(show != 0):
        print("Invert of", power, "in", phi, "is", invert)
        print("x = ", answer, "^", invert, "modulo", ring, " = ", x)

    return x


def exo20_21():
    """
    Alice and Bob use the RSA cryptosystem to exchange messages securely.
    """

    alice_pub = [133, 41]
    alice_priv = [133, 29]
    bob_pub = [187, 77]

    is_RSA_key_ok(alice_pub, 29)
    print(cipher_in_RSA([3], bob_pub, 1))
    print(cipher_in_RSA([10], alice_priv, 1))

    phiN = totient_faster(187, 1)
    print(invert_a_number_in_a_ring(77, phiN))


def exo23_24(na, ea, da, sa, nb, eb, db, sb, yab):
    """
    Altaïr and Bharani use the RSA cryptosystem.
    """

    da = invert_a_number_in_a_ring(ea, totient_faster(na, 1))
    db = invert_a_number_in_a_ring(eb, totient_faster(nb, 1))
    print("da = ", da, " db = ", db)

    generating_authentification_signature_from_A_to_B(
        [na, ea], [nb, eb], sa, da, 1)

    sign = check_authentification_signature_from_A_by_B(
        [nb, eb], [na, ea], yab, da, 1)

    if(sign == sb):
        print("yes")
    else:
        print("no")

    print("")


def exoChap3():
    """
    main for the exercise
    """
    print("exoChap3")

    exo23_24(209, 13, 0, 10, 221, 25, 0, 21, 98)
    exo23_24(77, 29, 0, 8, 65, 35, 0, 12, 98)

    #is_RSA_key_ok([2097101, 11111])

    #is_RSA_key_ok([2097101, 22221])

    # d = 772213
    # n = 25170253
    # e = invert_a_number_in_a_ring(d, totient_faster(n, 1))
    # print("e = ", e)
    # is_RSA_key_ok([n, e], d)

    # d = 762213
    # n = 25170253
    # e = invert_a_number_in_a_ring(d, totient_faster(n, 1))
    # print("e = ", e)
    # is_RSA_key_ok([n, e], d)

    # nc = 8207323
    # ec = 999501
    # mess = [102030]
    # x = cipher_in_RSA(mess, [nc, ec], 1)
    # y = cipher_in_RSA(mess, [nc, ec], 1)

    na = 2097101
    ea = 11111
    da = 338699

    nb = 25170253
    eb = 22720417
    db = 772213

    nc = 8207323
    ec = 999501

    # cipher_in_RSA([10000], [nb, eb], 1)

    # cipher_in_RSA([10000], [nb, db], 1)

    # cipher_in_RSA([12345], [na, ea], 1)
    # cipher_in_RSA([12345], [na, da], 1)

    sa = 256
    sb = 777
    sc = 1984

    dc = invert_a_number_in_a_ring(ec, totient_faster(nc))
    print("dc = ", dc)

    # generating_authentification_signature_from_A_to_B([nc, ec], [na, ea], sc, dc, 1)

    check_authentification_signature_from_A_by_B(
        [na, ea], [nc, ec], 2632215, dc, 1)


def main_chap3():
    """
        Main of the chapter 3
        Propose : 
            1 - calculate totient
            2 - calculate RSA key from p, q and e
            3 - check a RSA key with n and e
            4 - check a RSA key with n, e and d
            5 - check a RSA key with n and d
            6 - cipher in RSA
            7 - decipher in RSA
            8 - calculate a signature
            9 - check a signature
            10 - equation like x^5 = 41
            11 - pow mod
    """

    choice = 0
    while(choice != 99):

        print("What do you want to do : \n")
        print("1 - calculate totient")
        print("2 - calculate RSA key from p, q and e")
        print("3 - check a RSA key with n and e")
        print("4 - check a RSA key with n, e and d")
        print("5 - check a RSA key with n and d")
        print("6 - cipher in RSA")
        print("7 - decipher in RSA")
        print("8 - calculate a signature")
        print("9 - check a signature")
        print("10 - equation like x^5 = 41")
        print("11 - pow mod")

        print("\n99 - Quit\n")

        choice = int(input("Choice : "))

        # calculate totient
        if(choice == 1):
            n = int(input("n : "))
            print("\n")

            totient_faster(n, 1)

        # calculate RSA key from p, q and e
        elif(choice == 2):
            p = int(input("p : "))
            q = int(input("q : "))
            e = int(input("e : "))
            print("\n")

            calculate_RSA_key(p, q, e, 1)

        # check a RSA key with n and e
        elif(choice == 3):
            n = int(input("n : "))
            e = int(input("e : "))
            print("\n")

            is_RSA_key_ok([n, e])

        # check a RSA key with n, e and d
        elif(choice == 4):
            n = int(input("n : "))
            e = int(input("e : "))
            d = int(input("d : "))
            print("\n")

            is_RSA_key_ok([n, e], d)

        # check a RSA key with n and d
        elif(choice == 5):
            n = int(input("n : "))
            d = int(input("d : "))
            print("\n")

            e = invert_a_number_in_a_ring(d, totient_faster(n, 1))
            print("e = ", e)
            print("\n")

            is_RSA_key_ok([n, e], d)

        # cipher in RSA
        elif(choice == 6):
            print("Public key of the receiver : ")
            n = int(input("n : "))
            e = int(input("e : "))
            print("Message : ")
            numberOfValues = int(input("Number of values in the message : "))
            mess = ask_for_matrix(numberOfValues)
            print("\n")

            cipher_in_RSA(mess, [n, e], 1)

        # decipher in RSA
        elif(choice == 7):
            print("Private key of the receiver : ")
            n = int(input("n : "))
            d = int(input("d : "))
            print("Message : ")
            numberOfValues = int(input("Number of values in the message : "))
            mess = ask_for_matrix(numberOfValues)
            print("\n")

            cipher_in_RSA(mess, [n, d], 1)

        # calculate a signature
        elif(choice == 8):
            print("Public key of the sender (A) : ")
            na = int(input("na : "))
            ea = int(input("ea : "))

            print("\nPrivate key of the sender (A) : ")
            da = int(input("da (if you don't have it, write (-1)): "))

            print("\nSignature of the sender (A) : ")
            sa = int(input("sa : "))

            print("\nPublic key of the receiver (B) : ")
            nb = int(input("nb : "))
            eb = int(input("eb : "))

            print("\n")

            if(da == -1):
                da = invert_a_number_in_a_ring(ea, totient_faster(na))
                print("da = ", da)
                print("\n")

            generating_authentification_signature_from_A_to_B(
                [na, ea], [nb, eb], sa, da, 1)

        # check a signature
        elif(choice == 9):
            print("Public key of the sender (A) : ")
            na = int(input("na : "))
            ea = int(input("ea : "))

            print("\nPublic key of the receiver (B) : ")
            nb = int(input("nb : "))
            eb = int(input("eb : "))

            print("\nPrivate key of the receiver (B) : ")
            db = int(input("db (if you don't have it, write (-1)): "))

            print("\n")
            yab = int(input("Yab : "))

            print("\n")

            if(db == -1):
                db = invert_a_number_in_a_ring(eb, totient_faster(nb))
                print("db = ", db)
                print("\n")

            check_authentification_signature_from_A_by_B(
                [na, ea], [nb, eb], yab, db, 1)

        # equation like x^5 = 41
        elif(choice == 10):
            print("Equation be like : x^power = answer in Z/ringZ")
            power = int(input("power : "))
            answer = int(input("answer : "))
            ring = int(input("ring : "))
            print("\n")

            equations(power, answer, ring, 1)

        # pow mod
        elif(choice == 11):
            print("Calculation be like : x^y [mod]")
            x = int(input("x : "))
            y = int(input("y : "))
            mod = int(input("mod : "))
            print("\n")

            print(pow_mod(x, y, mod))

        elif(choice == 99):
            print("Bye")

        else:
            print("Error")

        print("\n\n")


if __name__ == "__main__":

    # # print(totient(14, 1))  # waiting : 6
    # # print(totient_faster(15, 1))  # waiting : 8

    # # print(calculate_RSA_key(23, 17, 43, 1))  # waiting : [ [391,43],[391,131] ]
    # # print(cipher_in_RSA([164, 28], [391, 43], 1))  # waiting : 284
    # # print(cipher_in_RSA([284, 267], [391, 131], 1))  # waiting : 164

    # #M = 115792089237316195423570985008687907853269984665640564039457584007908834671663
    # #E = 96514807760119017459957299373576180339312098253841362800539826362414936958669
    # #print(pow_mod(2, E, M))
    # #print(pow_mod(164, 43, 391))

    # # print(cipher_in_RSA([624345], [303632003, 1025771], 1))  # waiting : 164

    # # is_RSA_key_ok([47, 23])
    # # is_RSA_key_ok([143, 5])
    # # is_RSA_key_ok([143, 47])
    # # is_RSA_key_ok([143, 47], 29)
    # # is_RSA_key_ok([143, 17], 113)

    # print(generating_authentification_signature_from_A_to_B(
    #     [209, 107], [143, 17], 103, 143, 1))  # waiting : 114

    # print(check_authentification_signature_from_A_by_B(
    #     [209, 107], [143, 17], 114, 113, 1))  # waiting : 103

    # alice = [209, 13]
    # bob = [221, 25]
    # dAlice = 97
    # dBob = 169
    # sAlice = 10
    # sBob = 21

    # print(generating_authentification_signature_from_A_to_B(
    #     alice, bob, sAlice, dAlice))  # waiting : 186
    # print(check_authentification_signature_from_A_by_B(
    #     alice, bob, 186, dBob))  # waiting : 10

    main_chap3()
