emp_name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter Basic Salary: "))

# Salary calculations
hra = 0.20 * basic_salary   # 20% of Basic
da = 0.10 * basic_salary    # 10% of Basic
pf = 0.12 * basic_salary    # 12% of Basic

net_salary = basic_salary + hra + da - pf

print(f"Employee Name     : {emp_name}")
print(f"Employee ID       : {emp_id}")
print(f"Basic Salary      : ₹{basic_salary:.2f}")
print(f"HRA (20%)         : ₹{hra:.2f}")
print(f"DA (10%)          : ₹{da:.2f}")
print(f"PF (12%)          : ₹{pf:.2f}")
print("----------------------------")
print(f"Net Salary        : ₹{net_salary:.2f}")