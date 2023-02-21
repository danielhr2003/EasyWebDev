# Filename: readwithfor.py

linefeed = '\n'

file_object = open('helloworld.txt','r')

for inputLine in file_object:
    outputLine = inputLine.rstrip(linefeed)
    print(outputLine)

# Close the file
file_object.close()
