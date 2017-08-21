import time

#Calls primeEvens and primeOdds, then Returns maximum prime factor
def findMaxPrime(n,primes):
	primes = primeEvens(n,primes)
	primes = primeOdds(n,primes)
	return max(primes)

#Find Evens (All Factors of 2)
def primeEvens(n,primes):
	while (n % 2 == 0):
		n = n/2
		primes+= [2]
	return primes

#Find Odds (All Factors of 3 + 2n)
def primeOdds(n, primes):
	for p in range(3,n+1,2):
		while (n % p == 0):
			n = n/p
			primes+= [p]
	return primes

#Initializations
number = 27
primeFactors = []
print "Prime Factorization of " + str(number)

#Execute
start = time.time()
maxPrime = findMaxPrime(number, primeFactors)
elapsed = time.time() - start

#Display Results
print "Factorization: ",
print primeFactors
print "Largest Prime Factor: " + str(maxPrime)
print "Time elapsed: ",
print elapsed