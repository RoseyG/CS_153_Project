def bin_mul(A,B,P):
	b = bin(B)
	p = bin(P)
	c = 0
	for n in b:
		if int(n) == 1:
		c = c^(A<<(len(b)-1))
	
	return c

def add_sub(A, B):
	C = [int(n) for n in A]
	i = len(A) - len(B)
	for n in B:
		C[i] = C[i]^n
		i = i + 1
	func = "A(x) + B(x) = "
	i = 1
	for n in C:
		temp = str(n) + "x^"+ str(len(C) - i)
		func = func + temp
		if i < len(C):
			func = func + " + "
		i = i + 1
	print(func)
def mul(A, B, p):
	C = [0 for n in range(0,len(A) + len(B))]
	i = 0
	for m in B:
		j = i
		for n in A:
			temp = bin_mul(m,n,p)
			C[j] = C[j]^temp
		i = i + 1
	func = "A(x) x B(x) = "
	i = 1
	for n in C:
		temp = str(n) + "x^"+ str(len(C) - i)
		func = func + temp
		if i < len(C):
			func = func + " + "
		i = i + 1
	print(func)


while (True):
	not_valid = False
	print("Please enter your inputs:")
	A_x = [int(n) for n in raw_input("A(x): ").split()]
	B_x = [int(n) for n in raw_input("B(x): ").split()]
	P_x = [int(n) for n in raw_input("P(x): ").split()]

	print("You entered:")
	func = "A(x) = "
	i = 1
	for n in A_x:
		temp = str(n) + "x^"+ str(len(A_x) - i)
		func = func + temp
		if i < len(A_x):
			func = func + " + "
		i = i + 1
		if n >= pow(2,len(P_x) - 1):
			print(n)
			not_valid = True
	print(func)

	func = "B(x) = "
	i = 1
	for n in B_x:
		temp = str(n) + "x^"+ str(len(B_x) - i)
		func = func + temp
		if i < len(B_x):
			func = func + " + "
		i = i + 1
		if n >= pow(2,len(P_x) - 1):
			not_valid = True
	print(func)

	func = "P(x) = "
	i = 1
	for n in P_x:
		temp = str(n) + "x^"+ str(len(P_x) - i)
		func = func + temp
		if i < len(P_x):
			func = func + " + "
		i = i + 1
		if n > 1:
			not_valid = True
	print(func)
	print("GF(" + str(pow(2,len(P_x) - 1))+ ")")

	if not_valid:
		print("Your inputs are not valid, please enter another set of inputs.")
		continue

	p = 0
	i = 1
	for n in P_x:
		if n == 1:
			p = p + pow(2,len(P_x) - i)
		i = i + 1
	print("P in decimal: " + str(p))

	while(1):
		print("[1] Addition")
		print("[2] Subtraction")
		print("[3] Multiplication")
		print("[4] Division")
		print("[5] New input/Exit")
		
		choice = int(raw_input("Enter choice number: "))
		print("\n")
		if choice == 1:
			print("Addition:")
			add_sub(A_x,B_x)
		elif choice == 2:
			print("Subtraction")
			add_sub(A_x,B_x)
		elif choice == 3:
			print("Multiplication:")
		elif choice == 4:
			print("Division")
		elif choice == 5:
			break
		else:
			continue

	print("New input?")
	again = raw_input("[Y/y] to enter new inputs, [Enter] to exit: ")
	if (again == "Y") or (again == "y"):
		print("\n")
		continue
	else:
		break