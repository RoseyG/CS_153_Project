#include<stdio.h>

int main(){

	bool operate;
	char loop;
	int choice;
	string a_x;
	string b_x;
	string p_x;


	while(true){
		printf("Galois Field Calculator");

		// Get input
		printf("\nEnter A(x): ");
		scanf("%s", );
		printf("\nEnter B(x): ");
		scanf("%s", );
		printf("\nEnter P(x): ");
		scanf("%s", );

		// Validate input
		// if a_x[i], or b_x[i] >= 2^[sizeof(p_x)-1], invalid
		// if p_x[i] != (1||0), invalid
		
		operate = true;
		while(operate){
			// Menu
			printf("\nChoose an operation:");
			printf("\n[1] Addition");
			printf("\n[2] Subtraction");
			printf("\n[3] Multiplication");
			printf("\n[4] Division");
			scanf("%d", &choice);
			switch(choice){
				case 1:
					// Add/Subtract Function
				case 2:
					// Add/Subtract Function
				case 3:
					// Multiply Function
				case 4:
					// Divide Function
				case 5:
					operate = false;
				default:
					printf("\nPlease make a valid choice.");
			}
		}
	}
}


/**

(integers as bits)
Binary multiplication in GF:
	temp = zeroes
	loop for all b[i]:
		temp = temp xor a<<i if b[i] == 1
	xor with p_x(get decimal value?) until b is 3 bits or less
return answer in decimal

Polynomial addition in GF:

A[i] xor B[i], if they both exist. Copy what exists in only one polynomial

**/

