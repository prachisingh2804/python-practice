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
name = input("Enter your name: ")
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
total = calculate_total(m1, m2, m3)
percentage = calculate_percentage(total)
result = check_result(percentage)
print("----- Student Report -----")
print("Name:", name)
print("Total:", total)
print("Percentage:", round(percentage, 2), "%")
print("Result:", result)
