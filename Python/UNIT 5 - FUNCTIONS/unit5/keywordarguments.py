def sumThreeNumbers(number1, number2, number3):
    print("First Number:",number1)
    print("Second Number:",number2)
    print("Third Number:",number3)

def main():
    sumThreeNumbers(45, 23, 89)
    sumThreeNumbers(56, number3=78, number2=34)
    # sumThreeNumbers(number2=12,81,56) Causes syntax error, positional arg before keyword arg

main()
