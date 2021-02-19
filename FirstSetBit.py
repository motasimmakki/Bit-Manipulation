
num = int(input("\nEnter a Number : "))

def getfirstSetBit(num: int)->int:
	count = 1
	while not num%2:
		num >>= 1
		count += 1
	
	return count

# def getFirstSetBit(n: int):
#     if(n == 0):
#         return 0
#     return math.ceil(math.log2(n&-n)+1)

print("\nFirst Set Bit in", num, "is :",getfirstSetBit(num))
