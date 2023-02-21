# Filename: februarydays.py
# Author: George Cooke
# Date: September 28, 2021
# Program Desciption: Given a year, display if February has
#                     28 or 29 days.

# Input: year

# Processing: 1. Input year
#             2. If year divisible by 100 and year divible by 400
#                     leapYear = True
#             3. Else if year divisible by 4
#                     leapYear = True
#             4. Else
#                     leapYear = False
#             5. If leapYear
#                     Display 29 days
#                Else
#                     Display 28 day

# Output: days in February

print("Days in February")

year = int(input("Enter the year: "))

if year % 100 == 0 and year % 400 == 0:
    leapYear = True
elif year % 4 == 0 and not (year % 100 == 0):
    leapYear = True
else:
    leapYear = False

if leapYear:
    print("In", year, "February has 29 days")
else:
    print("In", year, "February has 28 days")
    
