#!/usr/bin/env python3



a ='y'

while a in ['Y', 'y'] or ['N', 'n']:	
	print ("\nAny more debits / deposits, Y/N?")
	a = input('> ')
	
	if a in ['Y', 'y']:
		print ("\nok")
		break
	elif a in ['N', 'n']:
		print ("\nquiting")
		break	
	else:
		print ("\nSorry didn't understand the input")
