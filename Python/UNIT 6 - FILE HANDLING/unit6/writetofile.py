# Filename: writetofile.py
# Author: George Cooke
# Date: November 16, 2021
# Program Description: Prompt user for their name and write to a text file.

# Input: User name
# Processing: 1. Prompt user for their name
#             2. Open a text file
#             3. Write user name to text file
#             4. Close text file
# Output: File with the user name

username = input('Enter your name: ')

# Create a new file on disk
file_object = open('username.txt','w')

# Write to the file
file_object.write(username)

# Close the file
file_object.close()
