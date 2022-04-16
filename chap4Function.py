"""
Function of the chapter 4

Based on the Mathematics for Cryptography class - Efrei Paris
Course from Nicolas Flasque & Federico Zalamea

Author of the program : Nausicaa68

"""

import math
import chap1Function as ch1f


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
