def binary_search(list,item):
	"""

		  					l   h
	arr = [1, 2, 3, 4,] 6, [10, 12, 15]

	l = m + 1
	h = 8
	item = 10
	
	m = 0 + 8 // 2 - 4
	arr[4] = 6

	n / 2 -- n / 2**2 -- n / 2**3 -- log2 X = n --> 2**n = x
	O (logn)

	"""
	low = 0
	high = len(list)-1

	while low<=high:
		mid_point= low + (high-low)//2
		# to return value
		midpoint_value=list[mid_point]
		if midpoint_value==item:
			return mid_point
		elif item<midpoint_value:
			high=mid_point -1
		else:
			low= mid_point+1

	return None

list=range(100,20000000)
item=1700 

print(binary_search(list,item))
