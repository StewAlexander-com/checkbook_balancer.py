import csv

nlist =["$210.00","$4150.30","$37.38"]
numtotal_2d ="$4,500"
StartNum_2d ="$6,500.00"

with open('checkbook.csv', 'w') as fd:
	fd.write(StartNum_2d)
	fd.write("\n")

with open('checkbook.csv', 'a') as f:
	writer = csv.writer(f)
	for e in nlist:
		writer.writerow([e])

with open('checkbook.csv', 'a') as fd:
	fd.write("----------\n")
	fd.write(numtotal_2d)
