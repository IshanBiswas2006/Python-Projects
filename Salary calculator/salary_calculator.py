basic_salary = float(input("Enter the Basic Salary: "))

hra = 0.10 * basic_salary
da = 0.20 * basic_salary
gross_salary = basic_salary + hra + da
pf = 0.12 * basic_salary
professional_tax = 200.0
net_salary = gross_salary - (pf + professional_tax)

print("\n--- Salary Details ---")
print(f"Basic Salary: {basic_salary:.2f}")
print(f"HRA (10%): {hra:.2f}")
print(f"DA (20%): {da:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")
print(f"PF (12%): {pf:.2f}")
print(f"Professional Tax: {professional_tax:.2f}")
print(f"Net Salary: {net_salary:.2f}")