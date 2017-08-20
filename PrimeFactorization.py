#Given a number
#Find the prime factorization

from numpy import prod
import time

def findPrimeFactor(n):
	for primeFactor in range(2,(n/2+1)):
		if (n % primeFactor == 0):
			return primeFactor
	return n

number = 5**12
primeFactors = [1]

start = time.time()

while (findPrimeFactor(number/prod(primeFactors)) != 1):
	primeFactors+= [findPrimeFactor(number/prod(primeFactors))]

elapsed = time.time() - start

print primeFactors
print str(elapsed) + " elapsed time"