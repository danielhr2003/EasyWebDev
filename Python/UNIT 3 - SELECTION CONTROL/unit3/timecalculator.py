# Filename: timecalculator.py
# Author: George Cooke
# Date: September 28, 2021
# Program Description: Calculate days, hours, mintes and
#                      seconds when given the number of seconds

# Input: Number of seconds

# Processing: 1. Input numberOfSeconds
#             2. If numberOfSeconds >= 86400
#                    Convert to days, hours, minutes, seconds
#                    Display days, hours, minutes, seconds
#             3. Else if numberOfSeconds >= 3600
#                    Convert to hours, minutes, seconds
#                    Display hours, minutes, seconds
#             4. Else if numberOfSeconds >= 60
#                    Convert minutes, seconds
#                    Display minutes, seconds
#             5. Else
#                    Display numberOfSeconds

# Output: days, hours, minutes, seconds

# Define constants
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

print("\nTime Calculator App\n")

numberOfSeconds = int(input("Enter the number of seconds: "))

if numberOfSeconds >= SECONDS_IN_DAY:
    # Convert to days, hours, minutes, seconds
    days = numberOfSeconds // SECONDS_IN_DAY
    remainder = numberOfSeconds % SECONDS_IN_DAY
    hours = remainder // SECONDS_IN_HOUR
    remainder = remainder % SECONDS_IN_HOUR
    minutes = remainder // SECONDS_IN_MINUTE
    seconds = remainder % SECONDS_IN_MINUTE
    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
elif numberOfSeconds >= SECONDS_IN_HOUR:
    # Convert to hours, minutes, seconds
    hours = numberOfSeconds // SECONDS_IN_HOUR
    remainder = numberOfSeconds % SECONDS_IN_HOUR
    minutes = remainder // SECONDS_IN_MINUTE
    seconds = remainder % SECONDS_IN_MINUTE
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
elif numberOfSeconds >= SECONDS_IN_MINUTE:
    # Convert to minutes, seconds
    minutes = numberOfSeconds // SECONDS_IN_MINUTE
    seconds = numberOfSeconds % SECONDS_IN_MINUTE
    print("Minutes:", minutes)
    print("Seconds:", seconds)
else:
    print("Seconds:", numberOfSeconds)
    
