#Runs Fibonnaci numbers as long as sum is less than the max
def fib(max):
	n=0
	a=1
	b=0
	sum=0
	while sum<max:
		sum=a+b
		b=a
		a=sum
		n+=1
		print sum
		if (sum % 2 == 0) :
			print " EVEN: " + str(sum)
	return n-1

#Computes Fibonnaci number
def compute(n):
	if (n==0 or n==1):
		return 1
	else:
		return compute(n-2) + compute(n-1)


ans = fib(3000000)
print "******"
print ans

check = compute(ans)
print check
