import time

min, max = 1901, 2000
days, months = [], []
numOfFirstMonthSundays=0

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

start = time.time()

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

#Sunday is day 7 of the week
#Using sieve method, make all multiples of 7s equal to 1
days[6:(weeks*7):7] = [1]*(weeks)

for x in range(len(days)):
	if months[x] == 1 and days[x] == 1:
		numOfFirstMonthSundays+=1

elapsed = time.time() - start

print "Days",
print len(days)
print "Weeks",
print weeks
print "Numer of Sundays that are the first day of the month:",
print numOfFirstMonthSundays
print "%s elapsed" %(elapsed)