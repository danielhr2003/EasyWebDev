# Filename: sentinel.py
# Author: George Cooke
# Date: October 19, 2021
# Program Description: Sum positive numbers

# Input: series of positive numbers
# Processing: 1. Set total to zero
#             2. Prompt for a number
#             3. while number greater than or equal to 0
#                    add number to total
#                    prompt for a number
#             4. Display total
# Output: Total of the series of positive numbers

total = 0
number = float(input("Enter a positive number (Negative to end): "))

while number >= 0:
    total += number
    number = float(input("Enter a positive number (Negative to end): "))

print("Total =",total)
