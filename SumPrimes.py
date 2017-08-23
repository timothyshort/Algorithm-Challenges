#This script sums the prime numbers through n

def is_prime(n):
	if n % 2 == 0:
		print "NOT PRIME: EVEN"
	else:
		for p in range (3,n/2,2):
			if n % p == 0:
				print "NOT PRIME: Divisible by " + str(p)
		print "PRIME:",
		return n


print is_prime(13)