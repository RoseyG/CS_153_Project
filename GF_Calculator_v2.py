def bin_mul(a,b,P,p):
	c = 0
	for i in range(0,len(P)-1):
		if pow(2,i)&b:
			c = c^(a<<i)
	i = 1
	while c >= pow(2,len(P)-1):
		if c&pow(2,2*(len(P)-1)-i):
			c = c^(p<<len(P)-1-i)
		i = i + 1
	return c

def add_sub(A, B):
	C = [0 for n in range(0,max(len(A),len(B)))]
	for n in range(1,len(C)+1):
		temp = ""
		if len(A)-n >= 0:
			C[len(C)-n] = C[len(C)-n]^A[len(A)-n]
			temp = temp + str(A[len(A)-n]) + "x^" + str(n-1)
		else:
			temp = temp + "0x^" + str(n-1)
		temp = temp + " + "
		if len(B)-n >= 0:
			C[len(C)-n] = C[len(C)-n]^B[len(B)-n]
			temp = temp + str(B[len(B)-n]) + "x^" + str(n-1)
		else:
			temp = temp + "0x^" + str(n-1)
		temp = temp + " = " + str(C[len(C)-n]) + "x^" + str(n-1)
		print(temp)
	func = "A(x) + B(x) = "
	i = 1
	for n in C:
		temp = str(n) + "x^"+ str(len(C) - i)
		func = func + temp
		if i < len(C):
			func = func + " + "
		i = i + 1
	print(func)

def mul(A, B, P, p):
	C = [0 for n in range(0,(len(A) + len(B)) - 1)]
	i = 0
	for m in B:
		j = i
		for n in A:
			temp = bin_mul(m,n,P,p)
			C[j] = C[j]^temp
			j = j + 1
		i = i + 1
	return(C)
def div(A, B, P, p):
	C = []
	a = [n for n in range(0,(len(A))]
	r = []
	while True:
		for i in range(0,p):
			c = bin_mul(i,B[0])
			if c == a[0]:
				break
		C.append[c]
		while len(C)


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
		print("\n")
		print("[1] Addition")
		print("[2] Subtraction")
		print("[3] Multiplication")
		print("[4] Division")
		print("[5] New input/Exit")
		
		choice = raw_input("Enter choice number: ")
		if choice == "1":
			print("Addition:")
			add_sub(A_x,B_x)
		elif choice == "2":
			print("Subtraction is the same as addition:")
			add_sub(A_x,B_x)
		elif choice == "3":
			print("Multiplication:")
			C = mul(A_x, B_x, P_x, p)
			func = "A(x) x B(x) = "
			i = 1
			for n in C:
				temp = str(n) + "x^"+ str(len(C) - i)
				func = func + temp
				if i < len(C):
					func = func + " + "
				i = i + 1
			print(func)
		elif choice == "4":
			print("Division")
			mul(A_x, B_x, P_x, p)
		elif choice == "5":
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