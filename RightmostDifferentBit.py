
num1 = int(input("\nEnter First Number : "))
num2 = int(input("Enter Second Number : "))

def getRightmostDifferentBit(num1: int, num2: int)->int:
	count = 1
	while (num1%2) == (num2%2):
		num1 >>= 1
		num2 >>= 1		
		count += 1

	return count

print("\nRightmost Different Bit in", num1, "and", num2, "is", getRightmostDifferentBit(num1, num2))