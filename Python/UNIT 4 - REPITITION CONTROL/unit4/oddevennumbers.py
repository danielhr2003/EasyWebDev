# Filename: oddevennumbers.py
# Author: George Cooke
# Date: October 19, 2021
# Program Description: Ask user for numbers and determine how many are odd and even

# Input: Numbers (multiple, need to loop)
# Processing: 1. Set keep_going to 'y'
#             2. while keep_going is y
#                    Prompt for an integer
#                    if integer is even
#                       add 1 to even_count
#                    else
#                       add 1 to odd_count
#                    Prompt if there are more numbers and save as keep_going
#             3. Display even_count and odd_count
# Output: Count of odd and even numbers entered

keep_going = "y"
even_count = 0
odd_count = 0

while keep_going == "y":
    number = int(input("Enter a whole number: "))
    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
    keep_going = input("More numbers? y/n ")

print("Even Numbers =", even_count)
print("Odd Numbers =", odd_count)
