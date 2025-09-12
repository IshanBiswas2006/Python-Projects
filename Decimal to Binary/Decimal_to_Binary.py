binary = input("Enter a binary number: ")

decimal = 0
for i in binary:
    if i not in '01':
        print("Invalid input. Please enter only 0s and 1s.")
        break
    decimal = decimal * 2 + int(i)
else:
    print(f"Decimal value: {decimal}")