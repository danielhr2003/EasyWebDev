# Filename: appendhelloworld.py
# Author: George Cooke
# Date: November 16, 2021
# Program Description: Append a line to a file

# Input: Existing file
# Processing: 1. Open a file
#             2. Append a new line
#             5. Close the file
# Output: File with a new line appended

linefeed = '\n'

# Open a file
file_object = open('helloworld.txt','a')

# Append to the file
file_object.write('Fourth line' + linefeed)

# Close the file
file_object.close()

print('Line appended to file')
