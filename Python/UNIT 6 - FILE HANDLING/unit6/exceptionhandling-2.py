# Filename: exceptionhandling-2.py
# Program Description: Examples of how to handle exceptions

# Example 2

try:
    file_object = open('hello.txt','r')

    inputLine = file_object.readline()

    file_object.close()

except FileNotFoundError as errorMessage:
    print(errorMessage)
except:
    print('Something went wrong!!!')

print('Program ends here')

