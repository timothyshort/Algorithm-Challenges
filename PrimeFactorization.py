#Given a number
#Find the prime factorization

from numpy import prod
import time

def findPrimeFactor(n):
	for primeFactor in range(2,(n/2+1)):
		if (n % primeFactor == 0):
			return primeFactor
	return n

def printPrimeFactorization(factors, n):
	print "Prime Factorization of " + str(n)
	for p in range(1,len(factors)):
		print str(factors[p]),
		if (p < len(factors)-1):
			print " x",
	print

number = 13195
primeFactors = [1]

start = time.time()

while (findPrimeFactor(number/prod(primeFactors)) != 1):
	primeFactors+= [findPrimeFactor(number/prod(primeFactors))]

elapsed = time.time() - start

#print primeFactors
printPrimeFactorization(primeFactors, number)
print str(elapsed) + " elapsed time"