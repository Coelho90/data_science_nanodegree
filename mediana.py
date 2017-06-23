def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    if len(numbers) % 2:
    	middle_index = int(len(numbers)/2)
    	return numbers[middle_index]
    else:
    	return (numbers[int(len(numbers)/2)-1] + numbers[int(len(numbers)/2)]) /2

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

numbers = [1,2,3,4]

if len(numbers) % 2 == True:
	print("Aqui é impar")
elif len(numbers) % 2 == False:
	print("aqui é par")

