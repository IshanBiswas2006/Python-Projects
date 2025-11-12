def main():
    MAX_ITEMS = 100
    prices = []
    total = 0.0

    print("Enter item prices (type 'done' to finish):")

    while len(prices) < MAX_ITEMS:
        user_input = input()

        if user_input.lower() == "done":
            break

        try:
            price = float(user_input)
            prices.append(price)
            total += price
        except ValueError:
            print("Invalid input. Try again.")

    # Round to 2 decimal places (like in C++ version)
    total = round(total + 1e-8, 2)

    print(f"Total Invoice Amount: {total}")


if __name__ == "__main__":
    main()
