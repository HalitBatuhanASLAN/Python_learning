def calculator():
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	choise = input("Enter one of the operation\n(+,-,*,/) : ")
	flag = 1
	while flag == 1:
		flag = 0
		if(choise == '+'):
			print(f"{num1} + {num2} = {num1 + num2}")
		elif(choise == '-'):
			print(f"{num1} - {num2} = {num1 - num2}")
		elif(choise == '*'):
			print(f"{num1} * {num2} = {num1 * num2}")
		elif(choise == '/'):
			print(f"{num1} / {num2} = {num1 / num2}")
		else:
			print("Please enter one of them")
			choise = input("Enter one of the operation\n(+,-,*,/) : ")
			flag = 1
while True:
	calculator()