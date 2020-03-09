nlist =['$210.00','$4,150.30','$37.38']
Nfile =open('checkbook.cvs','w')
numtotal_2d ="$4,500"

for element in  nlist:
	Nfile.write(element)
	Nfile.write(',')
Nfile.close()

with open('checkbook.cvs', 'a') as Nfile:
	Nfile.write(numtotal_2d)
