# !/usr/bin/env Python3

# Created by Larry nkengbeza
# Created on December 2020
# This program indicates the month in words based on numbers.

def main():
    # input
    month_number = int(input("Enter the number of the month: "))

    january = 1
    february = 2
    march = 3
    april = 4
    may = 5
    june = 6
    july = 7
    august = 8
    september = 9
    october = 10
    november = 11

    # Process and Output
    if month_number == january:
        print("The month  is January.")
    elif month_number == february:
        print("The Month is February")
    elif month_number == march:
        print("The month is March.")
    elif month_number == april:
        print("The month is April.")
    elif month_number == may:
        print("The month is May.")
    elif month_number == june:
        print("The month is June.")
    elif month_number == july:
        print("The month is July.")
    elif month_number == august:
        print("The month is August.")
    elif month_number == september:
        print("The month is September.")
    elif month_number == october:
        print(" the month is October.")
    elif month_number == november:
        print("The month is November.")
    else:
        print("The month is December")


if __name__ == "__main__":
    main()
