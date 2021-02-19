
num1 = int(input("\nEnter First Number : "))
num2 = int(input("Enter Second Number : "))

def differentBits(num1: int, num2: int)->int:
	count = 0
	while num1 or num2:
		if not ((num1%2) == (num2%2)):
			count += 1
		num1 >>= 1
		num2 >>= 1		

	return count

print("\nNo. of Bits Different in", num1, "and", num2, "are :", differentBits(num1, num2))