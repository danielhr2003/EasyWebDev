# Filename: poweroffour.py
# Author: George Cooke
# Date: October 19, 2021
# Program Description: Take a sequence of numbers and raise them to the power four

# Input: None
# Processing: 1. For number from 1 to 5
#                   Set powerfour to number to the power four
#                   Display powerfour
# Output: numbers raised to the power four

for number in range(1,6):
    powerfour = number ** 4
    print(number,"=",powerfour)
    
