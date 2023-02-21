theBoss = "Bruce Springsteen"

def showBoss():
    global theBoss
    print("The boss is",theBoss)
    theBoss = "Billy Joel"
    print("The new boss is",theBoss)

showBoss()
print("The actual boss is",theBoss)
