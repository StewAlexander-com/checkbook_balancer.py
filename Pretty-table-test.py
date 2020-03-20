#!/usr/bin/env python3

# From https://ptable.readthedocs.io/en/latest/tutorial.html

from prettytable import PrettyTable

t = PrettyTable()

start_num = 50
nlistmin_2d =[1,2,3,4,5]

t = PrettyTable ([start_num])
for e in nlistmin_2d:
	t.add_row([e])
print(t)
