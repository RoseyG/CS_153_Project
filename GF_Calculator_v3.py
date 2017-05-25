def bin_mul(a,b,P,p): # MULTIPLICATION
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

def add_sub(A, B, choice): # POLYNOMIAL ADDITION AND SUBTRACTION
	str_A = ""
	str_B = ""
	str_C = ""
	if choice == 1:
		line = "+"
	if choice == 2:
		line = "-"
	C = [0 for n in range(0,max(len(A),len(B)))]
	for n in range(1,len(C)+1):
		if len(A)-n >= 0:
			C[len(C)-n] = C[len(C)-n]^A[len(A)-n]
			str_A = "\t" + str(A[len(A)-n]) + str_A
		else:
			str_A = "\t " + str_A
		if len(B)-n >= 0:
			C[len(C)-n] = C[len(C)-n]^B[len(B)-n]
			str_B = "\t" + str(B[len(B)-n]) + str_B
		else:
			str_B = "\t " + str_B
		str_C = "\t" + str(C[len(C)-n]) + str_C
		line = line + "\t_______"
	print(str_A)
	print(str_B)
	print(line)
	print(str_C)
	return(C)

def mul(A, B, P, p): # POLYNOMIAL MULTIPLICATION
	C = [0 for n in range(0,(len(A) + len(B)) - 1)]
	i = 0
	for m in B:
		j = i
		print(str(m) + " x " + str(A) + ":")
		c = [0 for n in range(0,(len(A) + len(B)) - 1)]
		for n in A:
			c[j] = bin_mul(m,n,P,p)
			C[j] = C[j]^c[j]
			j = j + 1
		print(c)
		i = i + 1
	print(C)
	return(C)

def div(A, B, P, p): # POLYNOMIAL DIVISION
	R_Temp = [n for n in A]
	C = []
	while len(R_Temp) >= len(B):
		for i in range (0,p):
			if bin_mul(B[0],i,P,p) == R_Temp[0]:
				C.append(i)
				break
		print(str(i) + " x " + str(B) + ":")
		C_Temp = [bin_mul(i,B[j],P,p) for j in range (0,len(B))]
		while len(R_Temp) > len(C_Temp):
			C_Temp.append(0)
		R_Temp = add_sub(C_Temp,R_Temp,2)
		R_Temp.pop(0)
	return(C,R_Temp)

while (True):
	not_valid = False
	print("Please enter your inputs:")
	A_x = [int(n) for n in raw_input("A(x): ").split()]
	B_x = [int(n) for n in raw_input("B(x): ").split()]
	P_x = [int(n) for n in raw_input("P(x): ").split()]

	print("\n")
	print("You entered:") # DATA VALIDATION
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
		print("\n")
		if choice == "1":
			print("Addition:")
			C = add_sub(A_x,B_x,1)
			func = "A(x) + B(x) = "
		elif choice == "2":
			print("Subtraction:")
			C = add_sub(A_x,B_x,2)
			func = "A(x) - B(x) = "
		elif choice == "3":
			print("Multiplication:")
			C = mul(A_x, B_x, P_x, p)
			func = "A(x) * B(x) = "
		elif choice == "4":
			print("Division:")
			C,r = div(A_x, B_x, P_x, p)
			func = "A(x) / B(x) = "
			rem = "Remainder:"
			i = 1
			for n in r:
				temp = str(n) + "x^"+ str(len(r) - i)
				rem = rem + temp
				if i < len(r):
					rem = rem + " + "
				i = i + 1
			print(rem)
		elif choice == "5":
			break
		else:
			continue
		i = 1
		for n in C:
			temp = str(n) + "x^"+ str(len(C) - i)
			func = func + temp
			if i < len(C):
				func = func + " + "
			i = i + 1
		print(func)

	print("New input?")
	again = raw_input("[Y/y] to enter new inputs, [Enter] to exit: ")
	if (again == "Y") or (again == "y"):
		print("\n")
		continue
	else:
		break