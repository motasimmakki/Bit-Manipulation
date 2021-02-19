
n = int(input("\nEnter 'n' to find total Set Bits upto 'n' : "))

def getTotalSetBits(n: int)-> int:
	count = 0
	num = n
	if n == 1:
		return 1
	while n:
		if n%2:
			count += 1
		n >>= 1

	return (count + getTotalSetBits(num-1))

# def getTotalSetBits(n: int)-> int:
# 	count = 0
	
# 	while n >= 1:
# 		num = n
# 		while num:
# 			if num%2:
# 				count += 1
# 			num >>= 1
# 		n -= 1

# 	return count

# def getTotalSetBits(n: int)-> int:
#     n += 1
#     count = 0
    
#     x = 2
#     while x//2 < n:
        
#         quotient = n//x
#         count += quotient * x // 2
        
#         remainder = n % x
#         if remainder > x//2:
#             count += remainder - x//2
        
#         x = x*2
    
#     return count

print(getTotalSetBits(n))