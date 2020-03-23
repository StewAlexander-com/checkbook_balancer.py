#!/usr/bin/env python3

##############################################
# This program created by Stewart Alexander  #
# It is a simple checkbook balancer          #
##############################################

#Setting local currency from the "locale" module to US
import locale 
locale.setlocale( locale.LC_ALL, '')
'English_United States.1252'

# for exiting the program on a letter
import sys

#For saving the created contents to a CSV file
import csv

#for deleting Checkbook.txt if it exists before saving new data
import os

# Import PrettyTable for ascii printing
from prettytable import PrettyTable

# Import colors from termcolor
from termcolor import colored

# Creating table "t" from function PrettyTable
t = PrettyTable()

# Variable "nlist" that contains an empty list, isum to get around type issues.
nlist =[]
isum =[]
nlistmin_2d =[]
# Variable "sumlist" that contains the sum of the list
sumlist=0
# Variable "StartnNum" Original banking balance
StartNum =0
# Variable "a" to hold the answer (y,n) if there is another number
a =0
# Variable "s" to hold the next number value in the list
s =0
# Everything with "*_2d" is a variable to hold the amount formatted in US dollars

# The below asks for the original balance, enters it into "StartNum"
# If the user enters something other than a number, keep asking for one.

# Magenta prompt
prmpt_magenta = colored("> ",'magenta', attrs=['bold'])


# Header
print("\nThis program very simply balances your checkbook")
print("It will ask you for your orignal balance and any debits")
print ("- If you have a deposit, put a minus sign in front of the number")


while True:
	try:
		print("\nWhat is your orginal balance?")
		StartNum = float(input(prmpt_magenta))
	except ValueError:
		# If the input was something other than a number / float)
		print ("\n--- Sorry, we didn't understand the input ---\n")
	else:
		# no error, stop the loop
		break	

# Ask the user for the first number
# If the user enters something other than a number, keep asking for one

while True:
	try:
		print("\nWhat is the first debit (if deposit put a -)? ")
		Num1 = float(input(prmpt_magenta))
	except ValueError:
		print ("\n--- Sorry, we didn't understand the input ---\n")
	else:
		# no error, stop the loop
		break

# Format the float US Currency, place it in variable Num1_2d
Num1_2d = locale.currency(Num1, grouping =True)


# Add the first value to the lists (nlist for formatted numbers
# and isum for the sum) to get around type issues in python

isum.append(Num1)
nlist.append(Num1_2d)


# Ask if there is another number to add to the list from the user 


print ("\nAny more debits / deposits, Y/N?")
a = input(prmpt_magenta)

print ("\n")

# If the answer is yes, then request further inputs

if a in ['Y','y']:
	txtdes = colored("(Use a \"-\" for deposits, \"=\" when done, or \"q\" to quit)", 'green')
	print (txtdes)
	while True:
		amount_input = input(prmpt_magenta)
		
		# If the amount is a float / number:
		
		try:
			s = float(amount_input)
			# Format the float to US Currency, place it in variable s_2d
			s_2d = locale.currency(s, grouping =True)
			isum.append(s)
			nlist.append(s_2d)
			
		#If the input is an '=', end the loop
			
		except ValueError:
			if amount_input == "=":
				break
				
		#If the user types "q", just exit the program without continuing		
				
			elif amount_input =="q":
				sys.exit("\nQuitting...")
				
		#if the input is junk:
				
			else:
				print ("\n--- Sorry we didn't understand the input ---\n")

#Sum the list (to get around type issues, using the unformatted "s" list in "isum")
sumlist = sum(isum)

#Format sumlist to US Currency for printing purposes
sumlist_2d = locale.currency(sumlist, grouping =True)

#Printing a dividing line for clarity
txtline = colored("\n--------------------------------------------------------------",'cyan', attrs=['bold'])
print(txtline)

#Printing the formatted list, and the formatted total
if len(nlist) > 4:
	print ("\nThe numbers you entered are:\n")
	for x in range(len(nlist)):
		print(nlist[x])
	print ("---------")
else:
	print ("\nThe numbers you entered are:", nlist)

if sumlist > 0:
	red_sumlst = colored(sumlist_2d, 'red')
	print ("A total debit of: ",red_sumlst)
else:
	dep_sumlist = - sumlist
	depsumlist_2d = locale.currency(dep_sumlist, grouping =True)
	cyan_depsumlst = colored(depsumlist_2d, 'cyan')
	print ("A total deposit of: ",cyan_depsumlst)
	
	
#Subtract the "sumlist" (unformatted) from the "StartNum", save in in variable "numtotal" 
numtotal = StartNum - sumlist

# Formatting "numtotal" for printing purposes
numtotal_2d = locale.currency(numtotal, grouping =True)

# Formatting "StartNum" for printing purposes
StartNum_2d = locale.currency(StartNum, grouping =True)


if numtotal > 0:
	numtotal_2d =colored(numtotal_2d, 'cyan')
else:
	numtotal_2d = colored(numtotal_2d, 'red') 


# Printing the orginal balance - the sum (formatted), = the total (formatted)
print("\n")
print ("From what you entered:")
if sumlist > 0:
	print (StartNum_2d, "-",sumlist_2d,"=",numtotal_2d )
else:
	print (StartNum_2d, "+",depsumlist_2d,"=",numtotal_2d )

yellow_hash = colored("##########################################", 'yellow', 'on_grey')

print("\n")
print (yellow_hash)
print("Total remaining balance =",numtotal_2d)
print (yellow_hash, "\n")

#Creating a variable to store the current file location
Current_chkbtxt = './Checkbook.txt'

print ("Would you like to save this information Y/N?")
saveqt = input (prmpt_magenta)
if saveqt in ['Y','y']:
	
	#if the Checkbook.txt exists delete it
	if os.path.exists(Current_chkbtxt):
		os.remove(Current_chkbtxt)
		print ("\n-- Removed previous Checkbook.txt --\n")
	else:
		print ("\n")

	print("Saving data to Checkbook.txt ...")
	
	# Create a column with the starting value, the list of inputs, and the total
	
	# Creating first row, by concatinating the stings, ex. Org Bal: $50.32
	
	Org_bal = "Org Bal: "
	first_row = Org_bal + StartNum_2d
	
	#Coloring first row
	clr_frow = colored(first_row, 'green')

	
	# Entering the string as the first row to the table
	
	t = PrettyTable ([clr_frow])
	
	# Opening / Creating Checkbook.txt in order to write to it
	
	with open('Checkbook.txt', 'a') as f:
		writer = csv.writer(f)
		
		#Multiply the values in isum by -1, save in nlist_min
		#Solves the debt logic in the program so the output looks correct
		
		nlist_min = [i * -1 for i in isum]
		
		#Convert nlist_min into US dollars, and save in nlist_min_2d
		for e in nlist_min:
			e2 = locale.currency(e, grouping =True)
			nlistmin_2d.append(e2)
		
		#Print nlist_min_2d to Checkbook.txt as a PrettyTable
		
		for e in nlistmin_2d:
			t.add_row([e])
		writer.writerow([t])

	# Print total at the end of the table to Checkbook.txt
		
	with open('Checkbook.txt', 'a') as fd:
		fd.write("Total = ")
		fd.write(red_numtotal)
	
	# Tell the user the data is saved to Checkbook.txt, then gracefully exit the script
	
	sys.exit("\nSaved, quitting...")

# If the user doesn't want to save the data to Checkbook.txt, exit gracefully	
	
else:
	sys.exit("\nQuitting...")
