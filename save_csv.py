nlist =['$210.00','$4,150.30','$37.38']
Nfile =open('checkbook.csv','w')
numtotal_2d ="$4,500"
# save elements to  a file separated by 
for element in  nlist:
	Nfile.write(element)
	Nfile.write(',')
Nfile.close()

with open('checkbook.csv', 'a') as Nfile:
	Nfile.write(numtotal_2d)
