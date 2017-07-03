
import math
def nearest_square(number):
	"""
	returns the nearest square up to the passed number.
	"""
	if math.sqrt(number)%1 == 0:
		return number
	else:
		flag = True
		lower_number = number -1
		while flag:
			if math.sqrt(lower_number)%1 == 0:
				flag = False
			else: lower_number -= 1

		return lower_number




test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))