# A NL Chocolate Company employee claims processing system.
# Completed by: Darla Ward & Jeffrey Coles-Clarke
# Completed on:

import math
import datetime
import matplotlib.pyplot as plt

# Present the user with a menu and get them to input a number to choose one of the objects in the menu.
print("NL Chocolate Company")
print("Travel Claims Processing System")
print()
print("1. Enter an Employee Travel Claim.")
print("2. Fun Interview Question.")
print("3. Cool Stuff with Strings and Dates.")
print("4. Graph Monthly Claim Totals.")
print("5. Quit Program.")
print()

while True:
    Option = int(input("{:^37s}".format("Enter choice(1-5): ")))
    if Option == 1:
        # Enter Employee Travel Claim
        print(Option)
    elif Option == 2:
        # Fun Interview Question
        n = 1
        while n <= 100:
            if (n % 5) == 0 and (n % 8) == 0:
                print("FizzBuzz")
                n += 1
            elif (n % 5) == 0:
                print("Fizz")
                n += 1
            elif (n % 8) == 0:
                print("Buzz")
                n += 1
            elif (n % 5) == 0 and (n % 8) == 0:
                print("FizzBuzz")
                n += 1
            else:
                print(n)
                n += 1
        Continue = input("Press Enter to continue.")
        continue
    elif Option == 3:
        # Cool Stuff with Strings and Dates
        print(Option)
    elif Option == 4:
        #  Graph Monthly Claim Totals
        M = 0
        Month_arr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        TotalSales_arr = []

        while M <= 11:
            TotalSales_arr.append(float(input(f"Enter total sales for {Month_arr[M]}: ")))
            M += 1

        plt.plot(Month_arr, TotalSales_arr, color='magenta')

        plt.xlabel("Month")
        plt.ylabel("Total sales per month($)")

        plt.title("Monthly Claim Totals")
        plt.grid(True)

        plt.show()

        Continue = input("Press Enter to continue.")
        continue
    elif Option == 5:
        # Quit Program
        print()
        print("Program Exited")
        exit()
    else:
        print()
        print("Not a valid input. Please re-enter.")