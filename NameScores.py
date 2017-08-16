file = open('data/names.txt')
names = []
names = sorted(file.read().replace('"', '').split(','), key=str)
#names = ['TIM','COLIN','RICH']

lValue = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def nameValue(letter):
	for i in range(len(lValue)):
		if (lValue[i] == letter):
			return i+1

for row in range(len(names)):
	name = names[row]
	nameSum=0
	for char in range(len(name)):
		nameSum += nameValue(name[char])
	print name + " " + str(nameSum)