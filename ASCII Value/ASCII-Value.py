ch = input("Enter the Character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    i = ord(ch)
    print("\nASCII Value =", i)