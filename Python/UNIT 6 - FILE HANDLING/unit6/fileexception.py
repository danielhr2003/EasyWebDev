# Filename: fileexception.py

try:
    firstNumber = input('Enter a number: ')
    print(firstNumber / 3)

    file_object = open('hello.txt','r')

    firstLine = file_object.readline()
    print(firstLine)

    file_object.close()
except TypeError as errMessage:
    print(errMessage)
except FileNotFoundError:
    print('A file error occurred!!!')
except:
    print('Something went wrong!!!')
