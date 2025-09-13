def get_input_number():
    print("Choose input format:")
    print("1. Decimal")
    print("2. Binary")
    print("3. Hexadecimal")
    print("4. Octal")
    option = input("Enter option (1-4): ")

    value = input("Enter the number: ")

    try:
        match option:
            case "1": return int(value, 10)
            case "2": return int(value, 2)
            case "3": return int(value, 16)
            case "4": return int(value, 8)
            case _:
                print("Invalid input format.")
                return None
    except ValueError:
        print("Invalid number for selected format.")
        return None

def convert_and_display(number):
    print("\nChoose output format:")
    print("1. Decimal")
    print("2. Binary")
    print("3. Hexadecimal")
    print("4. Octal")
    option = input("Enter option (1-4): ")

    match option:
        case "1": print(f"Decimal: {number}")
        case "2": print(f"Binary: {bin(number)[2:]}")
        case "3": print(f"Hexadecimal: {hex(number)[2:].upper()}")
        case "4": print(f"Octal: {oct(number)[2:]}")
        case _: print("Invalid output format.")

def run_converter():
    print("Base Converter Tool")
    number = get_input_number()
    if number is not None:
        convert_and_display(number)


run_converter()