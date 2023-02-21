# Filename: average.py
# Author: George Cooke
# Date: October 19, 2021
# Program Description: Average a set of numbers given by a user

# Input: How many numbers, set of values
# Processing: 1. Prompt how many numbers
#             2. for number in 1 to how many numbers
#                    Prompt for a value
#                    Add value to total
#             3. average = total divided by how many numbers
#             4. Display average
# Output: average

total = 0

howManyNumbers = int(input("How many values? "))

for number in range(howManyNumbers):
    inputValue = float(input("Enter a value: "))
    total = total + inputValue

average = total / howManyNumbers

print("Average =",average)
