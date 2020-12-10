def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('First Number: '))
    number_2 = int(input('Second Number: '))

    if operation == '+':
   	    print('{} + {} = '.format(number_1, number_2))
   	    print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
	    print('{} / {} = '.format(number_1, number_2))
	    print(number_1 / number_2)

    else:
        print('Invalid operator used.')

    repeat()

def repeat():

	calc_repeat = input('''
	Another calculation? Y or N
	''')

	# Accept 'y' or 'Y' by adding str.upper()
	if calc_repeat.upper() == 'Y':
		calculate()

	    # Accept 'n' or 'N' by adding str.upper()
	elif calc_repeat.upper() == 'N':
	    print('Exiting.')

	else:
		again()

calculate()