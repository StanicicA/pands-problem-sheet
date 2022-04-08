#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

#You should create a function called <tt>sqrt</tt> that does this.

#I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

#I suggest that you look at the newton method at estimating square roots.
#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.
#Resource:https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.
#Author: Andrea Stanicic

input = float (input("Please enter a positive number:"))
print (input)

# Python3 implementation of the approach

# Function to return the square root of
# a number using Newtons method
def squareRoot(n, l) :

	# Assuming the sqrt of n as n only
	x = n

	# To count the number of iterations
	count = 0

	while (1) :
		count += 1

		# Calculate more closed x
		root = 0.5 * (x + (n / x))

		# Check for closeness
		if (abs(root - x) < l) :
			break

		# Update root
		x = root

	return root

# Driver code
if __name__ == "__main__" :

	n = 14.5
	l = 0.00001
print('The square root of {} is approx.{}'.format(input, squareRoot(n,l)))




