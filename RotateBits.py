
num = int(input("\nEnter a Number : "))
d = int(input("\nEnter value of 'd' : "))

def rotateBits(num: int, d: int)->list:
	rotation = [None]*2

	mask = 1
	i = 1
	while i < d:
		mask <<= 1
		mask += 1
		i += 1

	mask = (num & mask)
	
	rotation[0] = ((num << d) | (mask >> (16 - d))) 
	rotation[1] = ((num >> d) | (mask << (16 - d)))

	return rotation

print(rotateBits(num, d))
