import math


def invert_a_number_in_a_ring(number, n, s=1, t=0, N=0):
    return (n < 2 and t % N or invert_a_number_in_a_ring(n, number % n, t, s-number//n*t, N or n), -1)[n < 1]


def bring_a_number_in_a_ring(number, n):
    return number % n


if __name__ == "__main__":
    print(invert_a_number_in_a_ring(63, 10))  # waiting : 7
    print(bring_a_number_in_a_ring(-43, 7))  # waiting : 6
