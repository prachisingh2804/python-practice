secret = 7
guess = int(input("Enter your guess: "))

while guess != secret:
	if guess < secret:
		print("too low")
	else:
		print("too high")
	guess = int(input(" Enter your guess: "))

print("congratulations! you guessed it corretly")
	
