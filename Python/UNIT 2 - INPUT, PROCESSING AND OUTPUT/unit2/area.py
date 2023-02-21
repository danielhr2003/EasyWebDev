# Filename: area.py
# Date: September 7, 2021
# Author: George Cooke
# Program Description: Calculate the area of a rectangle.

# Input: length, breadth
# Processing: Prompt user for length and breadth
#             Area equals length times breadth
#             Display Area
# Output: Area

# Prompt the user for length and convert to float
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Calculate the area of the rectangle
area = length * breadth

# Display the aread of the rectangle
print("length =", length)
print("breadth =", breadth)
print("The area is", area,"cm")
