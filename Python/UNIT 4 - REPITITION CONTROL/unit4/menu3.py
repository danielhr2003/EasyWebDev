# Filename: menu3.py
# Author: George Cooke
# Date: October 19, 2021
# Program Description: Demonstrates a menu in program with an exit choice.
# This version user menu letter for choice instead of integer
# Uses OR statement for upper or lower case

menuChoice = " "

while menuChoice != "C" and menuChoice != "c":
    # Display menu
    print("A) See Rules\nB) Play Game\nC) Exit")

    # Prompt for choice
    menuChoice = input("Enter your choice: ")

    if menuChoice == "A" or menuChoice == "a":
        print("These are the rules.\n")
    elif menuChoice == "B" or menuChoice == "b":
        print("This is the game.\n")
    elif menuChoice == "C" or menuChoice == "c":
        print("Have a nice day!\n")
    else:
        print("Invalid choice. You must choose 1, 2 or 3\n")
