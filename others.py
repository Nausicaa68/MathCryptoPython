
"""
This function multiplies x with the number represented by res[].
res_size is size of res[] or*number of digits in the number represented by res[]. 
This function uses simple school mathematics for multiplication. 
This function may value of res_size and returns the new value of res_size

# This code is contributed by Anant Agarwal.

"""


def multiply(x, res, res_size):

    # Initialize carry
    carry = 0

    # One by one multiply n with individual digits of res[]
    for i in range(res_size):
        prod = res[i] * x + carry

        # Store last digit of 'prod' in res[]
        res[i] = prod % 10

        # Put rest in carry
        carry = prod // 10

    # Put carry in res and increase result size
    while (carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size += 1

    return res_size

# This function finds power of a number x


def power(x, n):

    MAX = 100000
    # printing value "1" for power = 0
    if (n == 0):
        return 1

    res = [0 for i in range(MAX)]
    res_size = 0
    temp = x

    # Initialize result
    while (temp != 0):
        res[res_size] = temp % 10
        res_size += 1
        temp = temp // 10

    # Multiply x n times
    # (x^n = x*x*x....n times)
    for i in range(2, n + 1):
        res_size = multiply(x, res, res_size)

    result = []
    for i in range(res_size - 1, -1, -1):
        result.append(res[i])

    return result


if __name__ == "__main__":

    print("\n", power(2, 110))
