# Employee Bonus Evaluation System

# Accept employee details
emp_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
rating = int(input("Enter Performance Rating (1–5): "))

# Bonus calculation based on rating
if rating == 5:
    bonus = 0.20 * salary
elif rating == 4:
    bonus = 0.15 * salary
elif rating == 3:
    bonus = 0.10 * salary
else:
    bonus = 0

final_salary = salary + bonus

# Display summary
print("\n------ Bonus Evaluation Summary ------")
print(f"Employee Name      : {emp_name}")
print(f"Performance Rating : {rating}")
print(f"Bonus Amount       : ₹{bonus:.2f}")
print(f"Final Salary       : ₹{final_salary:.2f}")
print("--------------------------------------")