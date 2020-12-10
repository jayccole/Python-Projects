print('''
Caluclator V0.1
Which would you like to do?
+ for Addition
- for Subtraction
* for Multiplication
/ for Division''')
operation = input(': ')

number_1 = int(input('First Number: '))
number_2 = int(input('Second Number: '))

#print(num_1)
#print(num_2)

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
    print('You have not typed a valid operator, please run the program again.')
