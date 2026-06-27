password = input("Enter your password: ")
characters = (len(password))
if characters < 6:
	print("weak password")
elif 6 <= characters <= 10:
	print("medium password")
else:
	print("strong password")
