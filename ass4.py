# Course Fee Billing System

# Accept course choice
print("Available Courses:")
print("1. Python Programming → ₹5000")
print("2. Data Analytics → ₹8000")
print("3. AI & ML → ₹12000")

course_choice = int(input("Enter course number (1/2/3): "))

# Assign course name and fee
if course_choice == 1:
    course_name = "Python Programming"
    fee = 5000
elif course_choice == 2:
    course_name = "Data Analytics"
    fee = 8000
elif course_choice == 3:
    course_name = "AI & ML"
    fee = 12000
else:
    print("Invalid course selection!")
    exit()

# Discount options
student = input("Are you a student? (yes/no): ").lower()
early = input("Early registration? (yes/no): ").lower()

# Calculate discounts
discount = 0
if student == "yes":
    discount += 0.10 * fee   # 10% student discount
if early == "yes":
    discount += 0.05 * fee   # 5% early registration discount

final_amount = fee - discount

# Display summary
print("\n------ Course Fee Summary ------")
print(f"Course Name        : {course_name}")
print(f"Original Fee       : ₹{fee:.2f}")
print(f"Total Discount     : ₹{discount:.2f}")
print(f"Final Payable Amt  : ₹{final_amount:.2f}")
print("--------------------------------")