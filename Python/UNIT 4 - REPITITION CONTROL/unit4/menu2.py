# Filename: menu2.py
# Author: George Cooke
# Date: October 19, 2021
# Program Description: Demonstrates a menu in program with an exit choice.
# This version user strings for choice instead of integer

menuChoice = "0"

while menuChoice != "3":
    # Display menu
    print("1) See Rules\n2) Play Game\n3) Exit")

    # Prompt for choice
    menuChoice = input("Enter your choice: ")

    if menuChoice == "1":
        print("These are the rules.\n")
    elif menuChoice == "2":
        print("This is the game.\n")
    elif menuChoice == "3":
        print("Have a nice day!\n")
    else:
        print("Invalid choice. You must choose 1, 2 or 3\n")
