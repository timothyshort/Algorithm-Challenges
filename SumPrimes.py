#This script sums the prime numbers through n

import time

#Method: Sieve of Eratosthenes
def is_prime_sieve(max):
	#Size of array not including 1, since 1 is not prime
	primes = range(2,max+1)
	maxRange = int(max**.5)+1

	for p in range (2, maxRange):
		primes[(2*p-2)::p] = [0] * (int((max/p))-1)
	print sum(primes)

#Method: Trial by Division
def is_prime(n):
	if (n==2):
		return True
	if n % 2 == 0:
		#print "NOT PRIME: EVEN"
		return False
	else:
		for p in range (3,int(n**.5)+1,2):
			if n % p == 0:
				#print "NOT PRIME: Divisible by " + str(p)
				return False
		return True


maxNumber = int(input("Enter the maximum number: "))

start = time.time()
is_prime_sieve(maxNumber)
elapsed = time.time() - start

"""
print "Prime Numbers: ",
sum=0
for num in xrange(2,maxNumber+1):
	if is_prime(num):
		print num,
		sum+= num
print "";
print "The sum of prime numbers below " + str(maxNumber) + ": " + str(sum)
"""

print "Elapsed Time:",
print elapsed