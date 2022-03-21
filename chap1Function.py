"""
Function based on the chapter 1
"""

import math


def is_prime(number):
    if(number > 1):
        for i in range(2, int(math.sqrt(number)) + 1):
            if (number % i == 0):
                return False
        return True
    else:
        return False


def prime_factors(n):
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


def GCD(a, b):
    if (a == 0):
        return b
    return GCD(b % a, a)

# Function to calculate LCM


def LCM(a, b):
    return (a * b) // GCD(a, b)

# Function to check if aelements in the array are pairwise coprime


def checkPairwiseCoPrime(listOfNumber):
    # Initialize variables
    prod = 1
    lcm = 1

    # Iterate over the array
    for i in range(len(listOfNumber)):
        # Calculate product of array elements
        prod *= listOfNumber[i]

        # Calculate LCM of array elements
        lcm = LCM(listOfNumber[i], lcm)

    # If the product of array elements
    # is equal to LCM of the array
    if (prod == lcm):
        return True
    else:
        return False


def invert_a_number_in_a_ring(number, n, s=1, t=0, N=0):
    return (n < 2 and t % N or invert_a_number_in_a_ring(n, number % n, t, s-number//n*t, N or n), -1)[n < 1]


# first return give the inverts and second return give all the invertible numbers
def find_all_invert_in_a_ring(n, show=0):
    all_invert = []
    all_invertible = []
    for i in range(n):
        invert = invert_a_number_in_a_ring(i, n)
        if(invert != -1):
            all_invert.append(invert)
            all_invertible.append(i)

    if(show != 0):
        print("Invertible number in Z/", n, "Z and their inverts : \nInvertibles = ",
              all_invertible, "\nInverts     = ", all_invert, "\n")

    return all_invert, all_invertible


def bring_a_number_in_a_ring(number, n):
    return number % n


if __name__ == "__main__":
    print(invert_a_number_in_a_ring(63, 10))  # waiting : 7
    print(invert_a_number_in_a_ring(3, 15))  # waiting : -1
    print(bring_a_number_in_a_ring(-43, 7))  # waiting : 6

    test = find_all_invert_in_a_ring(14)
    inverts = test[0]
    invertibles = test[1]
    print(inverts)  # waiting : 1,5,3,11,9,13
    print(invertibles)  # waiting : 1,3,5,9,11,13

    print(is_prime(23))  # waiting : true
    print(is_prime(2598))  # waiting : false
    print(is_prime(-2))  # waiting : false
    print(is_prime(7873))  # waiting : true

    print(prime_factors(350))  # waiting : 5 5

    list1 = [2, 3, 5]
    list2 = [2, 6, 7]
    print(checkPairwiseCoPrime(list1))  # waiting : true
    print(checkPairwiseCoPrime(list2))  # waiting : false

    