""" This isn't anything too fancy, but it is my first project and I'm proud
 of it!  """


"""
This is a basic calculator application. This app:

1) Prompts user which operation they would like to perform
2) Resquests the number of digits
3) Requests the digits to perform the operation
4) Reports the results and asks the user if they wish to do another operation

"""

import time

print "Welcome to the Calculator App!"

def select_op():

	operation = raw_input("What operation would you like to perform? (Enter A for addition, S for subtraction, M for multiplication, D for division, or X to exit.) ")
	operation = operation.lower()

	if operation == 'a':
		sum()
	elif operation == 's':
		subtract()
	elif operation == 'm':
		multiply()
	elif operation == 'd':
		divide()
	elif operation == 'x':
		quit()
	else:
		print "You must enter a valid input! Try again."
		select_op()


def sum():
	num_digits = raw_input("How many digits would you like to add? ")
	if is_float(num_digits):
		num_digits = float(num_digits)
	else:
		print "You must enter a valid input! Try again."
		sum()
	tracker = 0
	for i in range (0,int( num_digits)):
		digit = raw_input("Enter digit # %d. " % (i+1))
		if is_float(digit):
			digit = float(digit)
		else:
			print "You must enter a valid input!"
			sum()

		tracker += digit
	print "The sum is %.2f" % (tracker)
	repeat_op()

def subtract():
	num_digits = raw_input("How many digits would you like to subtract? ")
	first_digit = raw_input("Enter digit #1: ")
	if is_float(num_digits) and is_float(first_digit):
		num_digits = float(num_digits)
		first_digit = float(first_digit)
	else:
		print "You much enter a valid input!"
		subtract()

	for i in range(0, int(num_digits)-1):
		digit = raw_input("Enter digit #%d: " % (i+2))
		if is_float(digit):
			digit = float(digit)
		else:
			print "You entered an invalid number! Try again."
			subtract()

		first_digit -= digit
	print "The answer is %.2f" % (first_digit) 
	repeat_op()

def multiply():
	num_digits = raw_input("How many digits would you like to multiply? ")

	if is_float(num_digits):
		num_digits = float(num_digits)
	else:
		print "You much enter a valid input!"
		multiply()

	product = 1
	for i in range (0,int(num_digits)):
		digit = raw_input("Enter digit #%d: " % (i+1))
		if is_float(digit):
			digit = float(digit)
		else:
			print "You must enter a valid input! Try again."
			multiply()

		product *= digit
	print "The product is %.2f" % (product) 
	repeat_op()

def divide(): 
	num_digits = raw_input("How many times would you like to divide your first digit? ")
	first_digit = raw_input("Enter the first digit: ")
	if is_float(num_digits) and is_float(first_digit):
		num_digits = float(num_digits)
		first_digit = float(first_digit)
	else:
		print "You must enter a valid input! Try again."
	for i in range(0, int(num_digits)):
		digit = raw_input("Enter digit #%d: " % (i+2))

		if is_float(digit):
				digit = float(digit)
		else:
			print "You must enter a valid input! Try again."
			divide()

		first_digit /= float(digit)
	print "The answer is %.2f" % (first_digit) 
	repeat_op()

def quit ():
		print "Exiting calculator..."
		time.sleep(1)
		exit()

def repeat_op():
	response = raw_input("Would you like to do another operation? (Enter Y for yes or N for no) ")
	response = response.lower()
	if response == 'y':
		select_op()
	elif response == 'n':
		quit()
	else:
		print "You must enter a valid input! Try again."
		repeat_op()

def is_float(x): #Used to check valid input
	try:
		float(x)
		return True
	except ValueError:
		return False


select_op()