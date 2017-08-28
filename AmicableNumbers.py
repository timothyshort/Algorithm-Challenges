import time

max = int(input("Enter maximum number:"))
sumAmicableNumbers=0
list = [1] * (max)

start = time.time()

#Start at 2 and go until square root of n
#We only need to go the square root because for each a * b = n, we don't need b * a
for a in range(2, int (max**.5) +1):
	#Now find the sum of i and j where i * j = n
	for b in range (a, int (max/a)+1):
		list[a * b - 1] += a + b

#Now test if d(i)=j and d(j)=i
sums=0
for i in range(2,max):
	for j in range(i+1, max):
		if (list[i] == j+1 and list[j] == i+1):
			print i+1, list[i]
			print j+1, list[j]
			sums+= i+1 + j+1

elapsed = time.time() - start

print "Sum of Amicable Numbers 1 to " + str(max) + ":"
print sums
print "Time Elapsed:"
print elapsed

#n = int(input("Find sum of amicable number: "))
#print list[n-1]