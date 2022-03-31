from cmath import log
import cmath
import math
import re
from turtle import pu


def is_square(a):
    if(a == 1):
        return True
    x = a // 2
    seen = set([x])
    while(x * x != a):
        x = (x + (a // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


# Continued Fraction Expansion of Rationals


def continuous_fraction(a=0):
    result = []

    a = a.as_integer_ratio()
    nominator = a[0]
    denominator = a[1]

    #print(a, nominator, denominator)

    if(denominator != 1):

        q = nominator // denominator
        r = nominator % denominator
        result.append(q)

        for i in range(20):

            if(r != 0):
                nominator, denominator = denominator, r
                q = nominator // denominator
                r = nominator % denominator
                result.append(q)

    return result


def table(maximum=0):
    for i in range(1, maximum):
        print("√", i, "=", continuous_fraction(math.sqrt(i)))


def convergents(contFrac):
    nominators = []
    denominators = []
    convergents = []

    for i in range(20):

        if(i < len(contFrac)-1):

            if i == 0:
                ni = contFrac[i]
                di = 1
            elif i == 1:
                ni = 1 + (contFrac[i]*contFrac[i-1])
                di = contFrac[i]
            else:
                ni = nominators[i-2] + (contFrac[i]*nominators[i-1])
                di = denominators[i-2] + (contFrac[i]*denominators[i-1])

            nominators.append(ni)
            denominators.append(di)
            convergents.append(ni/di)

            # yield ni, di

    return nominators, denominators, convergents


def print_convergents(maximum=0):
    for i in range(1, maximum):
        print(i)
        if(is_square(i) == False):

            cfi = continuous_fraction(math.sqrt(i))
            conv_cfi = convergents(cfi)

            print(cfi, " = ", end="")
            for j in range(len(conv_cfi[0])):
                print(conv_cfi[0][j], "/", conv_cfi[1][j], end="")
                if(j != len(conv_cfi[0]) - 1):
                    print(" + ", end="")

            print(" = ", conv_cfi[2][len(conv_cfi[2])-1])


# def break_RSA(publicKey):

#     n = publicKey[1]
#     e = publicKey[0]
#     x = publicKey[0]/publicKey[1]

#     # f_ = continuous_fraction(x)
#     # c_ = convergents(f_)

#     # for k, dg in :
#     #     edg = e * dg
#     #     print(dg)
#     #     phi = edg // k
#     #     print(phi, edg, k)

#     #     x = n - phi + 1
#     #     if x % 2 == 0 and is_square((x // 2) ** 2 - n):
#     #         g = edg - phi * k
#     #         return dg // g
#     # return None

#     print(x)
#     cf_publicKey = continuous_fraction(x)
#     convergents_cf_publicKey = convergents(cf_publicKey)
#     print(cf_publicKey)
#     print(convergents_cf_publicKey)

#     for i in range(1, len(convergents_cf_publicKey[0])):

#         k = convergents_cf_publicKey[0][i]
#         dg = convergents_cf_publicKey[1][i]
#         # print(conv)

#     # for k, dg in conv:

#         edg = e * dg
#         print("dg = ", dg)
#         phi = edg // k
#         #print(phi, edg, k)

#         x = n - phi + 1
#         if x % 2 == 0 and is_square((x // 2) ** 2 - n):
#             g = edg - phi * k
#             return dg // g
#     return None


def break2(publicKey):

    n = publicKey[1]
    e = publicKey[0]

    x = e/n

    cf_ = continuous_fraction(x)

    print(cf_)


if __name__ == "__main__":
    print("Wiener Cryptanalysis")
    # print(continuous_fraction(math.sqrt(9)))

    # table(100)

    # print(convergents([1, 2, 2, 2, 2, 2, 2, 2, 2]))

    # print_convergents(100)

    #publicKey = [e,N]
    #print(break_RSA([2621, 8927]))

    print(break2([17993, 90581]))
