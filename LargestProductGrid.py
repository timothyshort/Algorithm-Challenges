import time

def maxHorz(data,maxData=0):

	for i in range(len(data)):
		rowData = [data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3] for j in range(0, len(data[0]) - 3)]
		maxData = max(max(rowData),maxData)
	return maxData

def maxVert(data,maxData=0):
	for j in range(len(data)):
		rowData = [data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j] for i in range(0, len(data[0])-3)]
		maxData = max(max(rowData),maxData)
	return maxData

def maxLowerDiag(data,maxData=0):
	#Find each 4-wise downward diagonal in each row
	for i in range(len(data)-3):
		rowData = [data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3] for j in range(0, len(data[0]) - 3)]
		maxData = max(max(rowData),maxData)
	return maxData

def maxUpperDiag(data,maxData=0):
	#Find each 4-wise upward diagonal in each row
	for i in range(3,len(data)):
		rowData = [data[i][j]*data[i-1][j+1]*data[i-2][j+2]*data[i-3][j+3] for j in range(0, len(data[0])-3)]
		maxData = max(max(rowData),maxData)
	return maxData

def getData():
	rows = []
	with open('data/LargestProductGrid-data.txt') as f:
	    for line in f:
	        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
	return rows

data = getData()

start = time.time()
maxProduct = max(maxHorz(data),maxVert(data),maxLowerDiag(data),maxUpperDiag(data))
elapsed = time.time()-start

print "Largest 4-Term Product in Grid:",
print maxProduct
print "Elapsed Time:",
print elapsed