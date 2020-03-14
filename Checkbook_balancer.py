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

# Header
print("\nThis program very simply balances your checkbook")
print("It will ask you for your orignal balance and any debits")
print ("- If you have a deposit, put a minus sign in front of the number")

while True:
	try:
		StartNum = float(input("\nWhat is your orginal balance? > "))
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
		Num1 = float(input("\nWhat is the first debit (if deposit put a -)? \n> "))
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


a = input("\nAny more debit / deposits? Y/N \n> ")

print ("\n")

# If the answer is yes, then request further inputs

if a in ['Y','y']:
	print ("(Use a \"-\" for deposits, \"=\" when done, or \"q\" to quit)")
	while True:
		amount_input = input(">   ")
		
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
print("\n--------------------------------------------------------------")

#Printing the formatted list, and the formatted total
if len(nlist) > 4:
	print ("\nThe numbers you entered are:\n")
	for x in range(len(nlist)):
		print(nlist[x])
	print ("---------")
else:
	print ("\nThe numbers you entered are:", nlist)

if sumlist > 0:
	print ("A Total debit of: ",sumlist_2d)
else:
	dep_sumlist = - sumlist
	depsumlist_2d = locale.currency(dep_sumlist, grouping =True)
	print ("A total deposit of: ",depsumlist_2d)
	
#Subtract the "sumlist" (unformatted) from the "StartNum", save in in variable "numtotal" 
numtotal = StartNum - sumlist

# Formatting "numtotal" for printing purposes
numtotal_2d = locale.currency(numtotal, grouping =True)

# Formatting "StartNum" for printing purposes
StartNum_2d = locale.currency(StartNum, grouping =True)

# Printing the orginal balance - the sum (formatted), = the total (formatted)
print("\n")
print ("From what you entered:")
if sumlist > 0:
	print (StartNum_2d, "-",sumlist_2d,"=",numtotal_2d )
else:
	print (StartNum_2d, "+",depsumlist_2d,"=",numtotal_2d )

print ("\n###################################################")
print("Total remaining balance =",numtotal_2d)
print ("###################################################")
print ("\n")

Current_chkbtxt = './Checkbook.txt'


saveqt = input ("Would you like to save this information Y/N?\n> ")
if saveqt in ['Y','y']:
	
	#if the Checkbook.txt exists delete it
	if os.path.exists(Current_chkbtxt):
		os.remove(Current_chkbtxt)
		print ("\n-- Removed previous Checkbook.txt --\n")
	else:
		print ("\n")

	print("Saving data to Checkbook.txt ...")
	
	# Create a column with the starting value, the list of inputs, and the total
	
	with open('Checkbook.txt', 'w') as fd:
		fd.write("Original Bal: ")
		fd.write(StartNum_2d)
		fd.write("\n----------\n")

	with open('Checkbook.txt', 'a') as f:
		writer = csv.writer(f)
		
		#Multiply the values in isum by -1, save in nlist_min
		#Solves the debt logic in the program so the output looks correct
		
		nlist_min = [i * -1 for i in isum]
		
		#Convert nlist_min into US dollars, and save in nlist_min_2d
		for e in nlist_min:
			e2 = locale.currency(e, grouping =True)
			nlistmin_2d.append(e2)
		
		#Print nlist_min_2d to Checkbook.txt
		
		for e in nlistmin_2d:
			writer.writerow([e])

	with open('Checkbook.txt', 'a') as fd:
		fd.write("----------\n")
		fd.write("Total = ")
		fd.write(numtotal_2d)
	
	sys.exit("\nSaved, quitting...")
	
else:
	sys.exit("\nQuitting...")
