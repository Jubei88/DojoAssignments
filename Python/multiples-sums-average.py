# Write code that prints all the odd numbers from 1 to 1000

for num in range(1,1000,2):
	print num

# prints all the multiples of 5 from 5 to 1,000,000

for num2 in range(5,1000000,5):
	print num2

# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
b = sum(a)/len(a)
print b