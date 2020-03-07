#!/usr/bin/env python3

##############################################
# This program created by Stewart Alexander  #
# It is a simple checkbook balancer          #
##############################################

#Setting local currency from the "locale" module to US
import locale 
locale.setlocale( locale.LC_ALL, '')
'English_United States.1252'

# Variable "nlist" that contains an empty list, isum to get around type issues.
nlist =[]
isum =[]
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
print ("If you have a deposit, add a minus sign in front of the number")

while True:
	try:
		StartNum = float(input("\nWhat is your orginal balance?  "))
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
		Num1 = float(input("What is the first debit (if deposit put a -)?  "))
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

a = input("Any more debit / deposits? Y/N  ")

# If the answer is yes, then request further inputs

if a in ['Y','y']:
	print ("(Use a \"-\" for deposit, or \"=\" when finished)\n")
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
print ("\nThe numbers you entered are", nlist)
if sumlist > 0:
	print ("A Total debit of ",sumlist_2d)
else:
	dep_sumlist = - sumlist
	depsumlist_2d = locale.currency(dep_sumlist, grouping =True)
	print ("A total deposit of ",depsumlist_2d)
	
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