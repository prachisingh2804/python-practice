def calculate_total(m1, m2, m3):
    return m1 + m2 + m3
def calculate_percentage(total):
    percentage = (total / 300) * 100
    return percentage
def check_result(percentage):
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"
def calculate_grade(percentage):
	if percentage >= 90:
		return "A+"
	elif percentage >= 80:
		return "A"
	elif percentage >= 70:
		return "B"
	elif percentage >= 60:
		return "C"
	elif percentage >= 40:
		return "D"
	else:
		return "F"
name = input("Enter your name: ")
def get_marks(subject):
    marks = int(input(f"Enter marks of Subject {subject}: "))
    while marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")
        marks = int(input(f"Enter marks of Subject {subject}: "))
    return marks
m1 = get_marks(1)
m2 = get_marks(2)
m3 = get_marks(3)
total = calculate_total(m1, m2, m3)
percentage = calculate_percentage(total)
result = check_result(percentage)
grade = calculate_grade(percentage)    
print("==============================")
print("      STUDENT REPORT")
print("==============================")
print("Name       :", name)
print("Total      :", total, "/300")
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
print("Result     :", result)
print("==============================")
