import time

#Find Evens (All Factors of 2)
def primeEvens(n):
	while (n % 2 == 0):
		n = n/2
		printPrime(2)
	primeOdds(n)

#Find Odds (All Factors of 3 + 2n)
def primeOdds(n):
	for p in range(3,n+1,2):
		while (n % p == 0):
			n = n/p
			printPrime(p)

def printPrime(prime):
	print str(prime) + " x",

number = 86
print "Prime Factorization of " + str(number)

start = time.time()
primeEvens(number)
elapsed = time.time() - start

print ""; print "Time elapsed: ",
print elapsed