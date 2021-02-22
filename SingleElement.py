
def getSingle(size: int, arr: list)-> int:
	arr = sorted(arr)
	if size%2:
		arr.append(0)
		size = len(arr)
	print(arr)
	i = 0
	while i < size-1:
		flag = True
		if i%2:
			flag = False
		if (arr[i] != arr[i+1]) and flag == True:
			return arr[i]

		i += 1

arr = [1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6]
# arr = [1, 2, 3, 2, 1]

print(getSingle(len(arr), arr))