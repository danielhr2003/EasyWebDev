# Filename: exceptionhandling.py
# Program Description: Examples of how to handle exceptions

# Example 1

try:
    userAge = int(input("Enter your age? "))

    if userAge == 21:
        print('You can purchase alcohol!!')
    elif userAge < 21:
        print('You are too young!!!')
except ValueError as errorMessage:
    print(errorMessage)
except:
    print('Something went wrong!!!')
else:
    print('No errors occured!!!')
finally:
    print('This is when an error occurs or not')

print('Program ends here')
