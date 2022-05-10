def my_function(input1, input2, input3):
	# type check 
	multiply = input1*input2*input3
	print('Multiplication: ', multiply)
	divide = input1/input2/input3
	print('Division: ', divide)
	add = input1+input2+input3 
	print('Addition: ', add)
	subtract = input1 - input2 - input3 
	print('Subtraction: ', subtract)

input1 = int(input('Please provide a number:'))
input2 = int(input('Another one please: '))
input3 = int(input('Another one please: '))
my_function(input1,input2,input3)
