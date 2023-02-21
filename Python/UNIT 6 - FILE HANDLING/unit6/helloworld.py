# Filename: helloworld.py
# Author: George Cooke
# Date: November 16, 2021
# Program Description: Write multiple lines to a file

# Input: None
# Processing: 1. Open a file
#             2. Write first line
#             3. Write second line
#             4. Write third
#             5. Close the file
# Output: File with first, second and third line

linefeed = '\n'

# Open a file
file_object = open('helloworld.txt','w')

# Write to the file
file_object.write('First line' + linefeed)
file_object.write('Second line' + linefeed)
file_object.write('Third line' + linefeed)

# Close the file
file_object.close()

print('helloworld.txt created!!!')

