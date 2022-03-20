"""
Function based on the chapter 3
"""
from chap1Function import *


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

    return phiN


if __name__ == "__main__":
    print(totient(14, 1))  # waiting : 6
    print(totient_faster(15, 1))  # waiting : 8
