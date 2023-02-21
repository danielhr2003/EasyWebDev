# Filename: readwithwhile.py
linefeed = '\n'

file_object = open('helloworld.txt','r')

# Read the first line
inputLine = file_object.readline()
inputLine = inputLine.rstrip(linefeed)
print(inputLine)

while inputLine != '':
    inputLine = file_object.readline()
    inputLine = inputLine.strip(linefeed)
    if inputLine != linefeed:
        print(inputLine)

# Close the file
file_object.close()
