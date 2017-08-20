#Given: n
#Find the sum of squares from 1 to n
#Find the square of the sum of numbers 1 to n
#Take the difference

import math

def sumSquares(n):
	squares = [(x**2) for x in range(1,n+1)]
	#print squares
	return sum(squares)

def squareSum(n):
	sums = [(x) for x in range(1,n+1)]
	#print sums
	return (sum(sums))**2

n=10
sumOfSquares = sumSquares(n)
print "The sum of the squares from 1 to " + str(n) + " : " + str(sumOfSquares)
squareOfSums = squareSum(n)
print "The square of the sum of numbers from 1 to " + str(n) + " : " + str(squareOfSums)

print "The difference between the two: " + str(squareOfSums - sumOfSquares)