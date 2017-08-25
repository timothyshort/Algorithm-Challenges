
def maxHorz(data):
	#rowData = [sum(data[0][i:i+4]) for i in range(0, cols - 3)]
	#rowData = [data[0][j]*data[0][j+1]*data[0][j+2]*data[0][3] for j in range(0, cols - 3)]

	for i in range(len(data)):
		rowData = [data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3] for j in range(0, len(data[0]) - 3)]
		print "ROW " + str(i+1) + str(rowData)
	return max(rowData)

def maxVert(data):
	for j in range(len(data)):
		rowData = [data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j] for i in range(0, len(data[0])-3)]
		print "COL " + str(j+1) + str(rowData)
	return max(rowData)

def maxLowerDiag(data):
	#Find each 4-wise downward diagonal in each row
	for i in range(len(data)-3):
		rowData = [data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3] for j in range(0, len(data[0]) - 3)]
		print "LOWER DIAG \ " + str(i+1) + str(rowData)
	return max(rowData)

def maxUpperDiag(data):
	#Find each 4-wise upward diagonal in each row
	for i in range(3,len(data)):
		rowData = [data[i][j]*data[i-1][j+1]*data[i-2][j+2]*data[i-3][j+3] for j in range(0, len(data[0])-3)]
		print "UPPER DIAG / " + str(i+1) + str(rowData)
	return max(rowData)



def getData():
	rows = []
	with open('data/LargestProductGrid-data.txt') as f:
	    for line in f:
	        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
	return rows

data = getData()
print data; print ""
print "ROWS: " + str(len(data))
print "COLS: " + str(len(data[0]))

print max(maxHorz(data),maxVert(data),maxLowerDiag(data),maxUpperDiag(data))
"""
m1 = maxHorz(data)
m2 = maxVert(data)
m3 = maxLowerDiag(data)
m4 = maxUpperDiag(data)
print max(m1,m2,m3,m4)
"""