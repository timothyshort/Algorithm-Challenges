#Finds multiples of a and b between 0 and range, where b > a
def findMultiples(a,b,max):
	sumA = findSum(a,max)
	sumB = findSum(b,max)
	print sumA + sumB


def findSum(number,max):
	sum=0
	multiple=0
	n=0
	while ((multiple + number) < max):
		n+=1
		multiple = number*n
		print multiple
		sum+=multiple
	return sum


findMultiples(3,5,10)
