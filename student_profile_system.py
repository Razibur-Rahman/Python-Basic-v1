# Student Profile System
print("=== Student Profile System ===\n")
# String (name)
name = input("Enter your name: ")
# Integer (age)
age = int(input("Enter your age: "))
# Float (GPA)
gpa = float(input("Enter your GPA: "))
# Boolean (is student)
is_student_input = input("Are you a student? (yes/no): ")

if is_student_input.lower() == "yes":
    is_student = True
else:
    is_student = False

# Output using string formating
print("\n--Your Profile--")
print("Name:",name)
print("Age:",age)
print(f"GPA: {gpa:.2f}")
print("Student Status:",is_student)

# Extra info
print("\n---Extra info---")
print("Name in uppercase:",name.upper())
print("Name length:",len(name))

# Condition check
if gpa >= 4.0:
    print("Result:Excellent Student")
elif gpa >= 3.5:
    print("Result: Good Student")
else:
    print("Result:Keep improving")
