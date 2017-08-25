
def maxHorz(data):
	#rowData = [sum(data[0][i:i+4]) for i in range(0, cols - 3)]
	#rowData = [data[0][j]*data[0][j+1]*data[0][j+2]*data[0][3] for j in range(0, cols - 3)]

	for i in range(len(data)):
		rowData = [data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3] for j in range(0, len(data[0]) - 3)]
		print "ROW " + str(i) + str(rowData)
	return max(rowData)

def maxVert(data):
	for j in range(len(data)):
		rowData = [data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j] for i in range(0, len(data[0])-3)]
		print "COL " + str(j) + str(rowData)
	return max(rowData)


def getData():
	rows = []
	with open('data/LargestProductGrid-data.txt') as f:
	    for line in f:
	        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
	return rows

data = getData()
print data; print ""
m1 = maxHorz(data)
m2 = maxVert(data)

print m1
print m2
print max(m1,m2)