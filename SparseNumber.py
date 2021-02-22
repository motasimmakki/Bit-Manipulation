
num = int(input("\nEnter a Number : "))

def isSparseNumber(num: int)->int:
	count = 0

	while num:
		if num%2:
			count += 1
		else:
			count = 0
		if count > 1:
			return False
		num >>= 1

	return True

print("\nNumber Status Is :", isSparseNumber(num))