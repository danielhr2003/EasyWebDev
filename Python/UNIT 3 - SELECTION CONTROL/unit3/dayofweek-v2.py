# Filename: dayofweek-v2.py
# Author: George Cooke
# Date: September 21, 2021
# Program Description: Given a number between 1 and 7, indicate the day of the week
#                      1 = Monday, 2 = Tuesday, ... 7 = Sunday

# Input: A number (1 - 7)
# Processing: 1. Prompt user for a number (1 - 7)
#             2. Determine the corresponding day of the week
#                     1 - Monday
#                     2 - Tuesday
#                     ...
#                     7 - Sunday
#             3. Display day of the week
# Output: The corresponding day of the week (Monday - Sunday)

# Intro
print("\nDays of the Week App\n")

# Prompt user for a number (1 - 7)
number = int(input("Please enter a number (1 - 7): "))

# Determine the corresponding day of the week
if number == 1:
    day = "Monday"
else:
    if number == 2:
        day = "Tuesday"
    else:
        if number == 3:
            day = "Wednesday"
        else:
            if number == 4:
                day = "Thursday"
            else:
                if number == 5:
                    day = "Friday"
                else:
                    if number == 6:
                        day = "Saturday"
                    else:
                        if number == 7:
                            day = "Sunday"
                        else:
                            day = None
                            print("Error ... Invalid number!!!")

# Display the corresponding day of the week
if day != None:
    print("The day ", number, " is ", day, sep="")
