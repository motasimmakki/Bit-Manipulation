
num = int(input("Enter a number to Toggle : "))

def getToggled(num: int)->int:
	toggledNum = 0

	i = 0 
	while num:
		mask = 1
		
		if not (num % 2):
			mask <<= i
			toggledNum |= mask

		num >>= 1
		i += 1

	return toggledNum

# num = 10
# num = 12
# num = 51

print("Toggeled Number of", num, "is", getToggled(num))

