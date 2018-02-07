

######################################################
# Quiz 1
######################################################

# problem 1

def ct1(x, y, z):
	print(x/y + x//y + int(x/y))
	print(y ** z + y%z)
	a = int(x) / int(y)
	return isinstance(a, int)

print(ct1(6, 4, 3))

# problem 2

def func1(x, y, z):
	print(x)
	return x//y + z

def func2(x, y, z):
	print(y)
	return func1(y*2, x+2, z-3)

def func3(x, y, z):
	print(z)
	return func2(z+5, x+3, y+2)

print(func3(7,4,2))

# problem 3

def rc1(n):x
	a = n % 10
	b = n % 100
	c = n // 1000
	return (b // 6*6) and (b == c + a) and (n > 1000) and (n < 2000)

# problem 4

def sumDigits(n):
	total = 0
	while (n // 10 != 0):
		total += n % 10
		n = n // 10
	total += n
	return total



######################################################
# Lab 1 + Practice
######################################################

def countMatchingDigits(x, y):
"""
Converts two integers into strings and counts how many of x's digits are in y's
"""
	count = 0
	x = str(x)
	y = str(y)
	for digit in x:
		if digit in y:
			count += 1
	return count

def getLength(n):
	count = 1
	while n//10 != 0:
		n = n // 10
		count += 1
	return(count)

def isPalindrome(n):
	
	# without using str() to check for length, we can use %10 and counter to check length
	length = getLength(n)
	div = length // 2
	
	# set subtotals for comparison
	total_a = 0
	total_b = 0
	
	# right side sum
	a = n % (10 ** div)
	
	if (length % 2 == 0):
		b = n // (10 ** div)
	else:
		b = n // (10 ** (div+1))
	
	result = (a == b)
	return result


######################################################
# HW 2
######################################################

def numberLength(x):
''' 
function that takes integer and converts into string
to count the length of digits
'''
	x = str(x)
	return len(x)

# problem 2

def containsOddDigits(x):
"""
Takes a number to check each digit for odd number
"""
	x = str(x)
	for digit in x:
		if (int(digit) % 2) == 1:
			return True
	return False


# problem 3

def countMultiplesOfSeven(a, b):
	
	total = 0	
	for number in range(a, b+1):
		if (number % 7 ) == 0:
			total += 1
	return total

# problem 4

def printNumberTriangle(n):

	for x in range(1, n+1):
		print(x, end = "")

		for y in range(x-1, 0, -1):
			print(y, end = "")

		print()


# problem 5
# leverage the property of pair of factors to check for prime efficiently

def isPrime(x):
	
	if (x % 2) == 0:
		return False
	if x < 2:
		return False
	if x == 2:
		return True
	for i in range(3, round(x ** .5) + 1, 2):
		if x % i == 0:
			return False
	return True


def sumOfSquaresOfDigits(n):
	
	total = 0
	n = str(n)
	for digit in n:
		total += int(digit) ** 2
	return(total)	


def isHappyNumber(n):
	
	happy_sum = n
	
	while happy_sum != 1 and happy_sum != 4:
		happy_sum = sumOfSquaresOfDigits(happy_sum)		
	
	if happy_sum == 1:
		return True
	elif happy_sum == 4:
		return False	
	else:
		return False


def nthHappyPrime(n):
	
	nthcount = 0
	number = 8
	
	while nthcount != n:
		if isPrime(number):
			if isHappyNumber(number):
				nthcount += 1
		number += 1

