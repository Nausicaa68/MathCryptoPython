from telnetlib import X3PAD
from chap2Function import *
from chap3Function import *

def five_letters_RSA(decipherednumber):
    one_mult = pow(29, 4) #first digit multiplier
    two_mult = pow(29, 3) #second digit multiplier
    three_mult = pow(29, 2) #third digit multiplier
    four_mult = pow(29, 1) #fourth digit multiplier
    five_mult = 1 #fifth digit multiplier

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0

    while(decipherednumber>= one_mult):
        decipherednumber-= one_mult
        one += 1
    while(decipherednumber>= two_mult):
        decipherednumber-= two_mult
        two += 1
    while(decipherednumber>= three_mult):
        decipherednumber-= three_mult
        three += 1
    while(decipherednumber>= four_mult):
        decipherednumber-= four_mult
        four += 1

    #while(decipherednumber>= five_mult):
    #    decipherednumber-= five_mult
    #    five += 1
    #then
    five = decipherednumber

    return [one,two,three,four,five] 


def convert_numbers_to_letters_28(array_five_numbers):
    #i=0
    new_array = ['-1', '-1', '-1', '-1', '-1']

    for i in range(5):
        if(array_five_numbers[i]+96 == 123):
            new_array[i] = "blank"
            #i +=1
        elif(array_five_numbers[i]+96 == 124):
            new_array[i] = "."
            #i +=1
        else:
            new_array[i] = chr(array_five_numbers[i]+96)
            #i +=1

    return new_array

def exercise_22():
    x1 = pow_mod(46509674,23719,73277933)
    
    print("first block :",x1)
    #print(five_letters_RSA(x1))
    print("The letters are: ", convert_numbers_to_letters_28(five_letters_RSA(x1))) #printing the array

    x2 = pow_mod(32695436,23719,73277933)
    print("second block :",x2)
    print("The letters are: ", convert_numbers_to_letters_28(five_letters_RSA(x2))) #printing the array

    x3 = pow_mod(59842725,23719,73277933)
    print("third block :",x3)
    print("The letters are: ", convert_numbers_to_letters_28(five_letters_RSA(x3))) #printing the array

    x4 = pow_mod(66944637,23719,73277933)
    print("fourth block :",x4)
    print("The letters are: ", convert_numbers_to_letters_28(five_letters_RSA(x4))) #printing the array
    
    x5 = pow_mod(2073634,23719,73277933)
    print("fifth block :",x5)
    print("The letters are: ", convert_numbers_to_letters_28(five_letters_RSA(x5))) #printing the array

    x6=pow_mod(8438724,23719,73277933)
    print("sixth block :",x6)
    print("The letters are: ", convert_numbers_to_letters_28(five_letters_RSA(x6))) #printing the array

    x7 = pow_mod(389483,23719,73277933)
    print("seventh block :",x7)
    print("The letters are: ", convert_numbers_to_letters_28(five_letters_RSA(x7))) #printing the array


import math
def primefactors(n):
   #even number divisible
   while n % 2 == 0:
      print (2),
      n = n / 2
    
   #n became odd
   for i in range(3,int(math.sqrt(n))+1,2):
     
      while (n % i == 0):
         print (i)
         n = n / i
    
   if n > 2:
      print (n)
 

def check_if_prime(num):
    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


if __name__ == "__main__":
    #main_chap2()
    exercise_22()

    #print (int(primefactors(73277933)))
    check_if_prime(1493)
    check_if_prime(49081)
 
