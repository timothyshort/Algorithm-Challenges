import time

def num_to_sum(a,b,c,d,e):
	sum = str(a) + str(b) + str(c) + str(d) + str(e)
	return int(sum)

sum=0

start = time.time()

for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			for d in range(0,10):
				for e in range(0,10):
					if ([a,b,c,d,e] == [1,1,1,1,1]): pass
					if num_to_sum(a,b,c,d,e) == a**5 + b**5 + c**5 + d**5 + e**5 :
						prod= a**5 + b**5 + c**5 + d**5 + e**5
						print prod,
						print "=",
						print a,
						print b,
						print c,
						print d,
						print e
						sum+= prod

elapsed = time.time() - start

print "%s found in %s" % (sum,elapsed)