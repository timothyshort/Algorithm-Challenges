def recursiveSum(data, row):
	for i in range(len(data[row])):
		#takes the larger of two sub-adjacent values and adds it to current value
		data[row][i] += max([data[row+1][i],data[row+1][i+1]])
	#base case
	if (row==1) :
		return data[row][0]
	else :
		return recursiveSum(data, row-1)
	



rows = []
with open('MaximumPathSumTriangle-data.txt') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])

print rows
result = recursiveSum(rows, len(rows)-2)
print result + rows[0][0]