#!/usr/bin/env python3

# This program takes in alist, creates a dictionary (moneyd) of an element list that = alist, and the alist values.
# Example: it takes "a","b","c","d","e" and "f", and creates 1,2,3,4,5,6; so that the dictionary
# has these key, value pairs {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f"}
# Then it requests the user to type in a key so as to edit its value pair
# (as in type in "1" and replace "a" with "hi")
# Then it takes the updated values and if they are different than the original list, replaces alist with these new
# values such that alist is now updated with the new values the user wants.
# By: Stewart Alexander 

alist = ["a", "b", "c", "d", "e", "f"]
key = []
valpair = []

def valprint():
	a = 1
	b = '.'
	for i in range(len(alist)):
		a_str = str(a)  # Converts the value stored in "a" to a string
		i_alist = alist[i]  # i_alist = element value of alist, so a = 1, b = 2, c = 3, etc
		key.append(a_str)  # Append the amount stored in "a" (a list of numbers starting at 1), to the list key
		valpair.append(i_alist)  # Append each element of list "alist"to list valpair, this is done for later, (a,b,c,etc)
		print(a_str + b, i_alist)  # Print the value in a_str (1,2,3, etc), followed by a ".", and the elements in i_alist (a,b,c) followed by a new line (1. a, 2. b, etc)
		a = a + 1  # Ups the amount stored in "a for every value stored in alist, so as to create a key that = (1,2,3,4,5,6)
	return (key, valpair)

print("\nThe original values are:")
valprint()  # Runs the function above, produces output easy to view for the user of "1.a, 2.b" etc)

moneyd = dict(zip(key, valpair))  # takes the lists key and valpair, and stores them as a dictionary

# Loops

more_val = 'y'

more_val = input(str("\nWould you like to change a value? Y/N?\n> "))

while more_val in ['Y', 'y'] or ['N', 'n']:

	if more_val in ['Y', 'y']:

		print("\nWhich value would you like to change, please type the number that corresponds to the value")
		key_input = str(input("> "))

		if key_input in moneyd:
			mk = moneyd[key_input]
			print (key_input, "=".strip(), mk)
			valchange = str(input("\nWhat is the value you would like to change it to?\n> "))
		else:
			print("\nThe value entered is not a listed number")
			print("\nWhich value would you like to change, please type the number that corresponds to the value")
			key_input = str(input("> "))
			valchange = str(input("\nWhat is the value you would like to change it to?\n> "))

		# To add: accept only numeric floats, if not a float, request the user to type a number

		# modifying elements of a dictionary
		moneyd[key_input] = valchange
		print("\n")
		print (key_input.strip(), f" is now \"{valchange}\"\n".strip())
		more_val = input(str("\nWould you like to change another value? Y/N?\n> "))

	elif more_val in ["N", "n"]:
		break
	else:
		print("\nSorry didn't understand the input\n")
		more_val = input(str("\nWould you like to change another value? Y/N?\n> "))


new_alist = list(moneyd.values())  # takes the value pairs of the updated dictionary and replaces alist with these values

check_lists = all(item in new_alist for item in alist)  # compares the lists

# If there were any changes to the liist, set the alist to the changes in new_alist

if check_lists is True:
	print ("\nOk, so no changes ...")
else:
	print("\nThe Updated list is:")
	alist = new_alist  # replaces alist with the new_alist, so as to continue
	valprint()  # reprints the new list in a way that is pleasing to the eye
