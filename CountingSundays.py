import time

#Add the index where month begins
def addMonths(a):
			months=[0]*(365+a)
			months[0] = 1
			months[27+a] = 1
			months[58+a] = 1
			months[88+a] = 1
			months[119+a] = 1
			months[149+a] = 1
			months[180+a] = 1
			months[211+a] = 1
			months[241+a] = 1
			months[272+a] = 1
			months[302+a] = 1
			months[333+a] = 1
			return months	

def findSundays():
	min, max = 1900, 2000
	days, months = [], []

	#Make an array of each day
	for n in range(min,max+1):
			if (n % 4 == 0):
				days+= [0]*366
				months+= addMonths(1)
			else:
				days+= [0]*365
				months+= addMonths(0)

	#Find the whole number of weeks (floor)
	weeks = int (len(days) / 7)

	#Sunday is day 7 of the week,	use sieve method
	days[6:(weeks*7):7] = [1]*(weeks)

	#Using LC method
	firstMonthSundays = [x for x in range(len(days[365:])) if (days[x] == 1 and months[x] == 1)]
	return len(firstMonthSundays)

start = time.time()
ans = findSundays()
elapsed = time.time() - start

print "%s found in %s elapsed" %(ans, elapsed)