def findPalindrome(digit):
	palindromes = [[]]
	maxNumber = 10**digit-1
	for x in range(maxNumber,maxNumber/10, -1):
		for y in range(x,maxNumber/10,-1):
			product = x*y
			if (str(product) == str(product)[::-1]):
				print "PALINDROME"
				palindromes+= [[x,y,product]]
				display(x,y,product)

def display(x,y,product):
	print str(x) + " x " + str(y) + " = " + str(product)


findPalindrome(3)
#print twoProducts