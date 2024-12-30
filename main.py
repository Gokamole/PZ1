# Main file of the project
# All rights are reserved
# ===============================================

# import all nessesary modules and libs
import is_even as ev # import module check 4etnoe
import sum as s # import module find sum of list
import complex.temperature as tem # import module corvertation from Cel to Farengeit
import math as m
from ..functions_lz import is_prime as pr

def main():
    user_choise = input("   Choose your function "
            "\n- if you want to check even choose 1 "
            "\n- if you want to check prime choose 2 "
            "\n- if you want to find sum of list choose 3 "
            "\n- if you want to convert temperature choose 4 "
            "\n     Your answer: ")
    if user_choise == "1":
        ev.main()
    elif user_choise == "2":
        pr.main()
    elif user_choise == "3":
        s.main()
    elif user_choise == "4":
        tem.main()
    else:
        print("Wrong answer")
        main()


if __name__ == '__main__':
    main()