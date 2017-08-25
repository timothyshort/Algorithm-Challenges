import time

def find(n):
	for a in range(1,n,1):
		for b in range(1,n,1):
				c = (n-a-b)
				if (a**2+b**2 == c**2):
					print "FOUND"
					return a, b, c

n = 1000

start = time.time()
(a,b,c) = find(n)
elapsed = time.time() - start

print "a = " + str(a) + " b = " + str(b) + " c = " + str(c)
print "a + b + c = " + str(a+b+c)
print "a**2 + b**2 = c**2 = " + str(c**2)
print "a * b * c = " + str(a*b*c)
print "Time elapsed:",
print elapsed