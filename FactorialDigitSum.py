import time

def fact(n):
	if (n==1 or n==0):
		return 1
	return fact(n-1) * n

def sum(number, n):
	print str(n) + "! = " + str(number)
	number = str(number)
	sumNumbers=0
	for i in number:
		#print int(i)
		sumNumbers += int(i)
	print "Some of digits = " + str(sumNumbers)

for num in range(10,0,-1):
	start = time.time()
	sumFactorial = sum(fact(num),num)
	elapsed = time.time() - start
	print "Solution: %s Time to execute: %s" % (sumFactorial, elapsed)
	print "********"