# Filename: readline.py
# Author: George Cooke
# Date: November 16, 2021
# Program Description: Read contents of a file line by line

# Input: File
# Processing: 1. Open the file
#             2. Read first line
#             3. Display first line read
#             4. Read second line
#             5. Display second line read
#             6. Read third line
#             7. Display third line read
#             8. Close the file
# Output: First three line of the file

linefeed = '\n'

# Open the file
file_object = open('helloworld.txt','r')

# Read the lines
firstLine = file_object.readline()
firstLine = firstLine.rstrip(linefeed)
print(firstLine)
secondLine = file_object.readline()
secondLine = secondLine.rstrip(linefeed)
print(secondLine)
thirdLine = file_object.readline()
thirdLine = thirdLine.rstrip(linefeed)
print(thirdLine)

# Close the file
file_object.close()
