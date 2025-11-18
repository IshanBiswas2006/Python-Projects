def table(x):
    for i in range(1, 11):
        print(f"{x} X {i} = {x * i}")

x = int(input("Enter number: "))
table(x)