!/usr/bin/env python3

# From https://ptable.readthedocs.io/en/latest/tutorial.html

from prettytable import PrettyTable
import csv

t = PrettyTable()

Org_bal = "Org Bal: "
StartNum_2d = 50
StartNum_Str = str(StartNum_2d)
first_row = Org_bal + StartNum_Str
nlistmin_2d =["$12.50",2,3,4,5]

t= PclerettyTable ([first_row])

with open('Checkbook.txt', 'a') as f:
	writer = csv.writer(f)
		
	for e in nlistmin_2d:
		t.add_row([e])
	writer.writerow([t])

