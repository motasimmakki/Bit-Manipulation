
num = int(input("\nEnter a Number : "))
k = int(input("\nEnter a value of k : "))

def isSet(num: int, k: int)->bool:
	mask = 1
	mask <<= k-1

	if mask&num:
		print("\nKth bit is Set.")
		return True
	print("\nKth bit is NOT Set.")
	return False

isSet(num, k)