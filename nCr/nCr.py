import math

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

if r > n or n < 0 or r < 0:
    print("Invalid input! Make sure 0 ≤ r ≤ n.")
else:
    ncr = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    print(f"{n}C{r} = {ncr}")
