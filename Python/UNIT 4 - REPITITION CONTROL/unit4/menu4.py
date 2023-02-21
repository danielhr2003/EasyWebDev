# Filename: menu3.py
# Author: George Cooke
# Date: October 19, 2021
# Program Description: Demonstrates a menu in program with an exit choice.
# This version user menu letter for choice instead of integer
# Convert choice to uppercase

menuChoice = " "

while menuChoice != "C":
    # Display menu
    print("A) See Rules\nB) Play Game\nC) Exit")

    # Prompt for choice
    menuChoice = input("Enter your choice: ")

    # Convert user's choice to uppercase
    menuChoice = menuChoice.upper()

    if menuChoice == "A":
        print("These are the rules.\n")
    elif menuChoice == "B":
        print("This is the game.\n")
    elif menuChoice == "C":
        print("Have a nice day!\n")
    else:
        print("Invalid choice. You must choose 1, 2 or 3\n")
