
num = int(input("\nEnter a Number : "))
k = int(input("Enter value of 'k' : "))

def setKthBit(num: int, k: int)->int:
	mask = 1
	mask <<= k
		
	return (num | mask)

print("\nAfter Setting the", k, "th bit, Number is :", setKthBit(num, k))