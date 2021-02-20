

num = int(input("\nEnter a Number: "))

def isPowerOfTwo(num: int)->bool:
	count = 0
	
	while num:
		if num%2:
			count += 1
		if count > 1:
			return False
		num >>= 1

	if count:
		return True

print("Status :", isPowerOfTwo(num))
