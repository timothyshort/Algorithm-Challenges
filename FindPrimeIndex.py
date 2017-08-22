import time

def findPrime(nth):
	primes=0
	i=1
	while (primes < nth):
		i+=1
		primes+=isPrime(i, nth)
	return i

def isPrime(number, nth):
	if (number == 1 or number == 2 or number == 3):
		#print "PRIME: " + str(number)
		return 1
	if (number % 2 == 0):
		return 0
	else:
		for p in range(3, number/2 + 1, 2):
			if (number % p == 0):
				return 0
	#print "PRIME: " + str(number)
	return 1

primeIndex = 10001
print "Finding the " + str(primeIndex) + " prime number:",
start = time.time()
n = findPrime(primeIndex)
elapsed = time.time() - start

print n
print "Elapsed:",
print elapsed