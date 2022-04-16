"""
    Exercise 22 from chapter 3
    Mathematics for Cryptography 

    Author : Nausicaa68
    
"""


def pow_mod(x, y, modulo):
    """
    Small function to calculate x^y [modulo]
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


def convert_number_from_base10_to_base29(number, base):
    """
    Convert "number" from the base 10 to the base "base"
    return a list with the unit in the base in a list
    """

    numberInBase = []

    while(number % base != 0):
        numberInBase.append(number % base)
        quotient = number // base
        number = quotient

    # we invert the number of the the list to have the right order
    return numberInBase[::-1]


def convert_numbers_to_letters(arrayOfNumber):
    """
    Convert the number to letter according the statement of the exercise 22
    """

    letters = []

    for i in range(len(arrayOfNumber)):
        if(arrayOfNumber[i] == 27):
            letters.append(" ")
        elif(arrayOfNumber[i] == 28):
            letters.append(".")
        else:
            letters.append(chr(arrayOfNumber[i] + 96))

    return letters


def exercise_22_deciphering(cypher, privateKey, show=0):
    """
    Decipher the exercise 22
    """

    decipher_text = ""

    for x in cypher:
        if(show != 0):
            decipher = pow_mod(x, privateKey[1], privateKey[0])
            print(x, "decipher is", decipher)
            print(decipher, "in base 29 is",
                  convert_number_from_base10_to_base29(decipher, 29))
            print("Letters : ", convert_numbers_to_letters(
                convert_number_from_base10_to_base29(decipher, 29)))
            print("")

        for letter in convert_numbers_to_letters(convert_number_from_base10_to_base29(pow_mod(x, privateKey[1], privateKey[0]), 29)):
            decipher_text += letter

    return decipher_text


def invert_a_number_in_a_ring(number, n, s=1, t=0, N=0):
    """
    recursive function to invert a number in Z/nZ
    """
    return (n < 2 and t % N or invert_a_number_in_a_ring(n, number % n, t, s-number//n*t, N or n), -1)[n < 1]


def prime_factors(n):
    """
    Function to find the prime factors of n
    """

    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def exercise_22_finding_publicKey(privateKey, show=0):
    """
    Calculate the public key of Anna in the exercise 22
    """

    primeFactor = prime_factors(privateKey[0])
    phi = (primeFactor[0] - 1) * (primeFactor[1] - 1)
    e = invert_a_number_in_a_ring(privateKey[1], phi)

    if(show != 0):
        print("Concidering Anna private key : ", privateKey)
        print("Prime factors : ", privateKey[0], "=", primeFactor)
        print("phi(", privateKey[0], ") = ", phi)
        print("e = invert of", privateKey[1], "in Z/", phi, "Z = ", e)
        print("")

    return [privateKey[0], e]  # [n, e]


if __name__ == "__main__":

    cypher = [46509674, 32695436, 59842725, 66944637, 2073634, 8438724, 389483]
    annaPrivateKey = [73277933, 23719]  # [n, d]

    print("decipher text : ", exercise_22_deciphering(
        cypher, annaPrivateKey, 1), "\n")
    print("Anna public key [n,e] : ", exercise_22_finding_publicKey(
        annaPrivateKey, 1), "\n")
