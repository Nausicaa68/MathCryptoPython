"""
Function based on the chapter 3
"""
from chap1Function import *


def pow_mod(x, y, modulo):
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
    invertibles = find_all_invert_in_a_ring(n)[1]
    phiN = len(invertibles)
    if(show != 0):
        print("Phi(", n, ") = ", end="")

    return phiN


def totient_faster(n, show=0):
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

    return phiN


def calculate_RSA_key(p, q, e, show=0):
    if(is_prime(p) and is_prime(q)):
        n = p*q
        phiN = (p-1)*(q-1)

        if(GCD(e, phiN)):
            d = invert_a_number_in_a_ring(e, phiN)

            if(show != 0):
                print("\nCalculate RSA key : ")
                print("n = p * q =", p, "*", q, " = ", n)
                print("Phi (", n, ") = (", p, "- 1) * (", q, "- 1) = ", phiN)
                print("d =", e, "(-1) in Z/", phiN, "Z  = ", d)
                print()

            return [[n, e], [n, d]]

        else:
            print("e (", e, ") is not coprime with phiN (", phiN, ")")
    else:
        print("p and/or q is/are not prime number")


def cipher_in_RSA(text, key, show=0):
    change_text = []
    for each in text:
        c = pow_mod(each, key[1], key[0])
        change_text.append(c)

        if(show != 0):
            print("c =", each, "^",
                  key[1], "[", key[0], "] = ", c)

    return change_text


def is_RSA_key_ok(publicKey, d=0):
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

    if(ok == 1):
        print("The key is ok")

    print()


def generating_authentification_signature_from_A_to_B(publicKeyA, publicKeyB, sA, dA, show=0):
    if(publicKeyA[0] < publicKeyB[0]):
        step1 = pow_mod(sA, dA, publicKeyA[0])
        step2 = pow_mod(step1, publicKeyB[1], publicKeyB[0])

        if(show != 0):
            print("step1 =", sA, "^",
                  dA, "[", publicKeyA[0], "] = ", step1)
            print("step2 =", step1, "^",
                  publicKeyB[1], "[", publicKeyB[0], "] = ", step2)

    elif(publicKeyA[0] > publicKeyB[0]):
        step1 = pow_mod(sA, publicKeyB[1], publicKeyB[0])
        step2 = pow_mod(step1, dA, publicKeyA[0])

        if(show != 0):
            print("step1 =", sA, "^",
                  publicKeyB[1], "[", publicKeyB[0], "] = ", step1)
            print("step2 =", step1, "^",
                  dA, "[", publicKeyA[0], "] = ", step2)

    return step2


def check_authentification_signature_from_A_by_B(publicKeyA, publicKeyB, yAB, dB, show=0):
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

    print(calculate_RSA_key())

