"""
Functions of the chapter 4

Based on the Mathematics for Cryptography class - Efrei Paris
Course from Nicolas Flasque & Federico Zalamea

Author of the program : Nausicaä

"""

import math
import chap1Function as ch1f


"""
To-do list : 

find all divisors of a number ex : 10 -> 1 2 5 10
find inverses and order of all the element of a group
-> when a^x % n = 1
find generators (when ord(g) = |G|)

"""


def main_chap4():

    choice = 0
    while(choice != 99):

        print("What do you want to do : \n")
        print("1 - nothing for now")

        print("\n99 - Quit\n")

        choice = int(input("Choice : "))

        # nothing for now
        if(choice == 1):
            print("nothing")

        elif(choice == 99):
            print("Bye")

        else:
            print("Error")

        print("\n\n")


if __name__ == "__main__":

    print("Chap4")
    main_chap4()
