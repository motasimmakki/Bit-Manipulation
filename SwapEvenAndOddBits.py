
num = int(input("\nEnter a Number : "))

# def swapEvenOddBits(num: int)-> int:
	
# 	if num == 2:
# 		return num>>1

# 	number = num
# 	evenMask = 0
# 	oddMask = 0

# 	i = 0
# 	while number:
# 		evenMask <<= 1
# 		oddMask <<= 1
# 		if i%2:
# 			# Even Bit Mask.
# 			evenMask += 1
# 		else:
# 			# Odd Bit Mask.
# 			oddMask += 1
# 		number >>= 1
# 		i += 1
# 	print(evenMask)
# 	print(oddMask)

# 	evenMask = (evenMask & num)
# 	oddMask = (oddMask & num)

# 	evenMask >>= 1
# 	oddMask <<= 1

# 	return (evenMask | oddMask)

def swapEvenOddBits(num: int)-> int:
	
	evenMask = (num & 0xAAAAAAAA)
	oddMask = (num & 0x55555555)

	evenMask >>= 1
	oddMask <<= 1

	return (evenMask | oddMask)

print("\nAfter Swapping Even and Odd bits the Number is :", swapEvenOddBits(num))