def functionOne():
    print("My Student ID is shefay9008")


def functionTwo():
    firstNumber = int(input("Please enter a number: "))
    secondNumber = int(input("Please enter a number: "))
    sumValue = firstNumber + secondNumber
    print(f"The sum of {firstNumber} and {secondNumber} is {sumValue}.")
    return sumValue


def functionThree(sumValue):
    if sumValue > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 9008


def main():
    functionOne()
    sumValue = functionTwo()
    returnedValue = functionThree(sumValue)
    print(f"functionThree returned the value of {returnedValue}.")


main()
