# A NL Chocolate Company employee claims processing system.
# Completed by: Darla Ward & Jeffrey Coles-Clarke
# Completed on: 2022-06-20

import datetime
import matplotlib.pyplot as plt


def Menu():
    # Present the user with a menu.
    print()
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print("1. Enter an Employee Travel Claim.")
    print("2. Fun Interview Question.")
    print("3. Cool Stuff with Strings and Dates.")
    print("4. Graph Monthly Claim Totals.")
    print("5. Quit Program.")
    print()


def BonusAmntReceiptCalculation():
    # A function to calculate the Bonus Amount for the Employee Travel Claim. Multiple if statements using Trp_Length,
    # Kms_Travelled, Car_Type, Claim_Type, Strt_Date.month and Strt_Date.day. Returns Bonus_Amnt.

    Bonus_Amnt = 0
    if Trp_Length > 3:
        Bonus_Amnt += 100
    else:
        pass

    if Kms_Travelled > 1000 and Car_Type == "O":
        Bonus_Amnt += (Kms_Travelled * 0.04)
    else:
        pass

    if Claim_Type == "E":
        Bonus_Amnt += (Trp_Length * 45)
    else:
        pass

    if Strt_Date.month == 12 and Strt_Date.day in range(15, 22):
        Bonus_Amnt += (Trp_Length * 50)
    else:
        pass

    return Bonus_Amnt


# Constants
TC_DAY_RATE = 85
TC_OWNED_KM_RATE = .17
TC_RENTED_PD_RATE = 65
TC_HST_RATE = 0.15

Menu()

while True:
    Option = int(input("{:^37s}".format("Enter choice(1-5): ")))
    if Option == 1:
        # Enter Employee Travel Claim
        while True:  # Validation Input Loops
            while True:  # Loop for Employee Number Validation
                try:
                    Emp_Num = int(input("Enter the Employee Number(5 digits):"))
                    if len(str(Emp_Num)) != 5:  # Check if Employee Number is correct length
                        print("Please enter a valid Employee Number.")
                    else:
                        break
                except:
                    print("Please enter a valid Employee Number.")
            while True:  # Loop for first name validation
                Emp_Fnam = input("Enter the Employee's first name:").upper()
                if Emp_Fnam == "":
                    print("Employee first name cannot be blank, please re-enter.")
                else:
                    break
            while True:  # Loop for name validation
                Emp_Lnam = input("Enter the Employee's last name:").upper()
                if Emp_Lnam == "":
                    print("Employee last name cannot be blank, please re-enter.")
                else:
                    break
            Trp_Loc = input("Enter the Trip Location: ")
            while True:  # Start Date Validation Loop
                try:
                    Strt_Date = input("Enter the trip start date (yyyy-mm-dd): ")
                    Strt_Date = datetime.datetime.strptime(Strt_Date, "%Y-%m-%d")
                except:
                    print("Start date must be in the form yyyy-mm-dd")
                else:
                    break
            while True:  # End Date Validation Loop
                try:
                    End_Date = input("Enter the trip end date (yyyy-mm-dd): ")
                    End_Date = datetime.datetime.strptime(End_Date, "%Y-%m-%d")
                except:
                    print("End date must be in the form yyyy-mm-dd")
                else:
                    if End_Date.day > Strt_Date.day + 7:
                        print("Trip end date cannot be more than 7 days after the start date.")
                    else:
                        break
            Trp_Length = End_Date.day - Strt_Date.day
            while True:  # Car validation
                Car_Type = input("Type (O) if the car was the Employee's, or type (R) if the car was rented: ").upper()
                if Car_Type.upper() != "O" and Car_Type.upper() != "R":
                    print("Please enter a valid option for car type.")
                else:
                    break
            while True:  # Kms travelled Loop
                try:
                    Kms_Travelled = int(input("Enter the Kms travelled during the trip: "))
                except:
                    print("Please enter a valid amount")
                else:
                    if Kms_Travelled > 2000:
                        print("Kms travelled cannot exceed 2000, please re-enter.")
                    else:
                        break
            while True:  # Claim Type Validation
                Claim_Type = input("Type (S) for a Standard claim, or type (E) for an Executive claim: ").upper()
                if Claim_Type.upper() != "S" and Claim_Type.upper() != "E":
                    print("Please enter a valid option for claim type.")
                else:
                    break

            Per_Diem_Amnt = Trp_Length * TC_DAY_RATE
            if Car_Type == "R":
                Milage_Amnt = TC_RENTED_PD_RATE * Trp_Length
            else:
                Milage_Amnt = Kms_Travelled * TC_OWNED_KM_RATE
                pass
            Bonus_Amnt = BonusAmntReceiptCalculation()
            Claim_Amnt = Per_Diem_Amnt + Milage_Amnt + Bonus_Amnt
            Hst_Chrg = Per_Diem_Amnt * TC_HST_RATE
            Claim_Total = Claim_Amnt + Hst_Chrg

            Claim_Total_Dsp = "${:,.2f}".format(Claim_Total)
            Hst_Chrg_Dsp = "${:,.2f}".format(Hst_Chrg)
            Claim_Amnt_Dsp = "${:,.2f}".format(Claim_Amnt)
            Bonus_Amnt_Dsp = "${:,.2f}".format(Bonus_Amnt)
            Per_Diem_Amnt_Dsp = "${:,.2f}".format(Per_Diem_Amnt)

            if Milage_Amnt > 0:
                Milage_Amnt_Dsp = "${:,.2f}".format(Milage_Amnt)
            else:
                Milage_Amnt_Dsp = "N/A"
                pass

            print()
            print(f"Start Date: {Strt_Date.year},{Strt_Date.month},{Strt_Date.day}")
            print(f"End Date:   {End_Date.year},{End_Date.month},{End_Date.day}")
            print(f"Employee No.: {Emp_Num:<10}")
            print(f"Trip Location:{Trp_Loc:<10}")
            print("Employee Info:")
            print(f"            {Emp_Fnam:<13}. {Emp_Lnam:<13}")
            print()
            print("Car Details: ")
            print(f"Car owned (O) or Rented (R):          {Car_Type:<1}")
            print(f"Standard Claim (S) or Executive (E):  {Claim_Type:<1}")
            print("-" * 40)
            print(f"Per Diem Amnt:             {Per_Diem_Amnt_Dsp:>10}")
            print(f"Mileage Amount:            {Milage_Amnt_Dsp:>10}")
            print(f"Bonus Amount:              {Bonus_Amnt_Dsp:>10}")
            print("{:^40s}".format("-" * 10))
            print(f"Claim Amount:               {Claim_Amnt_Dsp:>10}")
            print(f"Hst:                        {Hst_Chrg_Dsp:>10}")
            print(f"Claim Total:                {Claim_Total_Dsp:>10}")
            print(" " * 10, "-" * 10)

            while True:
                validate = input("Continue with another purchase? ( Y | N ): ").upper()
                if validate != "Y" and validate != "N":
                    print("Must enter Y or N.")
                else:
                    break
            if validate == "N":
                break
        Continue = input("Press Enter to continue.")
        continue
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
        while True:
            while True:  # Loop for first name validation
                Fnam = input("Enter the Employee's first name:").upper()
                if Fnam == "":
                    print("Employee first name cannot be blank, please re-enter.")
                else:
                    break
            while True:  # Loop for last name validation
                Lnam = input("Enter the Employee's last name:").upper()
                if Lnam == "":
                    print("Employee first last cannot be blank, please re-enter.")
                else:
                    break
            while True:  # Loop for Phone Number Validation
                try:
                    Phone_Num = int(input("Enter the Employee Phone Number:"))
                    if len(str(Phone_Num)) != 10:  # Check if Phone Number is correct length
                        print("Please enter a valid Phone Number.")
                    else:
                        break
                except:
                    print()
            while True:  # Current Date Validation Loop
                try:
                    Curr_Date = input("Enter the Current date (yyyy-mm-dd): ")
                    Curr_Date = datetime.datetime.strptime(Curr_Date, "%Y-%m-%d")
                except:
                    print("Date must be in the form yyyy-mm-dd")
                else:
                    break
            while True:  # Start Date Validation Loop
                try:
                    Strt_Date = input("Enter the Start date (yyyy-mm-dd): ")
                    Strt_Date = datetime.datetime.strptime(Strt_Date, "%Y-%m-%d")
                except:
                    print("Date must be in the form yyyy-mm-dd")
                else:
                    break
            while True:  # Birth Date Validation Loop
                try:
                    Birf_Date = input("Enter your the date of your next birthday (yyyy-mm-dd): ")
                    Birf_Date = datetime.datetime.strptime(Birf_Date, "%Y-%m-%d")
                except:
                    print("Date must be in the form yyyy-mm-dd")
                else:
                    break
            # Backwards First Name I Guess
            Reversed_Fanm = []
            Fnam_Len = len(Fnam)
            while Fnam_Len > 0:
                Reversed_Fanm += Fnam[Fnam_Len - 1]
                Fnam_Len = Fnam_Len - 1
            # Phone Number divided by the length of first name
            Pnum_Dsp = Phone_Num / len(Fnam)
            # Last name but Vertical Backwards again
            Reversed_Lanm = []
            Lnam_Len = len(Lnam)
            while Lnam_Len > 0:
                Reversed_Lanm += Lnam[Lnam_Len - 1]
                Lnam_Len = Lnam_Len - 1
            #           print(" ".join(Reversed_Lnam))
            # Months until Bday but in tally marks
            Num_Months = (Birf_Date.year - Curr_Date.year) * 12 + (Birf_Date.month - Curr_Date.month)
            Num_Months_Dsp = "I" * Num_Months
            # Seconds Worked by employee
            Wrkd_Days = (Curr_Date.year - Strt_Date.year) * 365 + (Curr_Date.month - Strt_Date.month) * 30
            Wrkd_Days = Wrkd_Days + (Curr_Date.day - Strt_Date.day)
            Wrkd_Seconds = Wrkd_Days * 86400

            print()
            print(f"Current Date:                           {Curr_Date.year}-{Curr_Date.month}-{Curr_Date.day}")
            print(f"Start Date:                             {Strt_Date.year}-{Strt_Date.month}-{Strt_Date.day}")
            print(f"Birth Date:                             {Birf_Date.year}-{Birf_Date.month}-{Birf_Date.day}")
            print(f"First Name:                             {Fnam}")
            print(f"Last Name:                              {Lnam}")
            print(f"Phone Number:                           {Phone_Num}")
            print("'Cool' Stuff I Did")
            print()
            print(f"Phone No. Divided by First Name Length: {Pnum_Dsp}")
            print(f"First Name Backwards:")
            print(" ".join(Reversed_Fanm))
            print("Last Name Backwards:          ")
            print(" ".join(Reversed_Lanm))
            print(f"Number of Months until B-Day:{Num_Months_Dsp}")
            print(f"Number of Seconds Worked:    {Wrkd_Seconds}")

            while True:
                validate = input("Continue with another employee? ( Y | N ): ").upper()
                if validate != "Y" and validate != "N":
                    print("Must enter Y or N.")
                else:
                    break
            if validate == "N":
                break
        Continue = input("Press Enter to continue.")
        continue
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
        # Exit Program
        print()
        print("Program Exited")
        exit()
    else:
        print()
        print("Not a valid input. Please re-enter.")
