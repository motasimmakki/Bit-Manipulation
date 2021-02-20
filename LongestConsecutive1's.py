
num = int(input("\nEnter a Number : "))

def getLongestConsecutiveOnes(num: int)->int:

	prevCount = 0
	count = 0

	while num:
		if num%2:
			count += 1
		else:
			if prevCount < count:
				prevCount = count
			count = 0
		num >>= 1

	return count if (count > prevCount) else prevCount

print("\nLongest Consecutive 1's are :", getLongestConsecutiveOnes(num))