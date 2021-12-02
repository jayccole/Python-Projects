# User selects number
print('Choose a number and I\'ll take it to 1!')
print('Enter number:')
try:
	number = int(input())
# Does the main job of collatz sequencing
	while number >= 2:
		if (number % 2) == 0:
			number = (number // 2)
			print(number)
		else:
			number = (number * 3 + 1)
			print(number)
except:
	print("Numbers only please")