def F_to_C(f):
    return 5*(f-32)/9

f=int(input("Enter temp in F: "))
a=F_to_C(f)

print(f"{round(a,2)}°C")