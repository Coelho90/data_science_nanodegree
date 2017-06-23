def top_three(input_list):

	top_three = sorted(input_list, reverse=True)
	print(top_three)
	return top_three[:3]



list = [2, 3, 5, 6, 8, 4, 2, 1]

print(top_three(list))