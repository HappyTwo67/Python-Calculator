print("This is a simple addition calculator")

try:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))

    num3 = num1 + num2

    print("The answer is", num3)

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