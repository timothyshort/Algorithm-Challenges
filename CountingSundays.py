import time

min, max = 1901, 1901
days = []
months = []

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

#Make an array of each day
for n in range(min,max+1):
		if (n % 4 == 0):
			days+= [0]*366
			months+= addMonths(1)
		else:
			days+= [0]*365
			months+= addMonths(1)

print ""
print "Days",
print len(days)
weeks = int (len(days) / 7)
print "Weeks",
print weeks

days[6:(weeks*7):7] = [1]*(weeks)

print "Number of Sundays in 20th Century:",
print sum(days)

sundays=0
for n in range(min,max+1):
	sundays+=sum(days[n:n+30])

print sundays