# Filename: exceptionhandling-3.py
# Program Description: Examples of how to handle exceptions

# Example 3

linefeed = '\n'
filename = input('Enter a file name: ')

while filename != '':
    try:
        # Open file
        file_object = open(filename,'r')

        # Process file
        for inputLine in file_object:
            outputLine = inputLine.rstrip(linefeed)
            print(outputLine)

        # Close file
        file_object.close()
        filename = ''
    except FileNotFoundError:
        filename = input('Enter a filename (blank to quit program): ')

print('Program ends here')

