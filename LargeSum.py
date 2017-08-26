import time

def getData():
	#Read the data file
	filename = 'data/LargeSum-data.txt'
	sums=0
	with open(filename) as ins:
	  for line in ins:
	    sums+= int(line)
	#Return the sum
	return sums

start = time.time()
sumNums = getData()
ans = sumNums / (10**(len(str(sumNums))-10))
elapsed = time.time()-start

print sumNums
print "First 10 digits:",
print ans
print "Elapsed Time:",
print elapsed