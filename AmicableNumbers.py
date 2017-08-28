import time

max = int(input("Enter maximum number:"))
list = [1] * (max)

t1 = time.time()

#Start at 2 and go until square root of n
#We only need to go the square root because for each a * b = n, we don't need b * a
for a in range(2, int (max**.5) +1):
	#Sieve method
	#Now find the sum of i and j where i * j = n
	for b in range (a, int (max/a)+1):
		list[a * b - 1] += a + b

t2 = time.time()

#Now test if d(i)=j and d(j)=i
sumAmicableNumbers=0
for i in range(2,max):
	if list[i] < max and list[i] < i:
		j = list[i]
		if (list[j-1] == i+1) :
			sumAmicableNumbers+= i+1 +j

t3 = time.time()

print("Sum of Amicable Numbers 1 to %s: %s") % (max, sumAmicableNumbers)
print("%s time elapsed to find Product Pairs") % (t2-t1)
print("%s time elapsed to find Amicable Number Sums") % (t3-t2)
print("%s total elapsed time") % (t3-t1)