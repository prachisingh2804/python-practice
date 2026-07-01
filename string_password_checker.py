password = input("Enter your password: ")

print("Length:", len(password))

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
if "@" in password or "#" in password:
    print("Special character found!")
else:
    print("No special character found.")
