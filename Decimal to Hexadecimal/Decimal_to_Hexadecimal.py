def DecToHex(d):
    h = int(d)
    return hex(h)

print("Enter Decimal Number: ", end="")
dn = input()

hdn = DecToHex(dn)
print("\nEquivalent Hexadecimal Value = ", hdn[2:].upper())