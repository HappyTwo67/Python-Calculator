print("This is a simple subtraction calculator")

try:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))

    if num1 > num2:
        num3 = num1 - num2
    else:
        num3 = num2 -num1

    print("The answer is", num3, "in non-negative order")

    import pyperclip

    copycheck = input("Copy result? (Y/N): ").upper()

    if copycheck == "Y":
        pyperclip.copy(str(num3))
        print("Result copied to clipboard!")
    elif copycheck == "N":
        print("Ok.")
    else:
        print("That isn't Y or N")

except ValueError:
    print("That is not a number")