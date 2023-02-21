currentYear = 2021

# Uses global because there is no local 'currentYear'
def showCurrentYear():
    print("Inside showCurrentYear():",currentYear)

# Variable 'currentYear' is redefined as a local
def showPreviousYear():
    currentYear = 2020
    print("Inside showPreviousYear():",currentYear)

# Uses the global keyword to modify global 'currentYear'
def showNextYear():
    global currentYear
    currentYear = 2022
    print("Inside showNextYear():",currentYear)

print("Current Year:",currentYear)
showCurrentYear()
print("Current Year:",currentYear)
showPreviousYear()
print("Current Year:",currentYear)
showNextYear()
print("Current Year:",currentYear)

