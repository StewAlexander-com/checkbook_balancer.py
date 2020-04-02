#!/usr/bin/env python3

# This program takes list "alist", createss a list of numbers (i_alist) = to alist, and stores them as a dictionary
# for example if the key list is (a,b,c,d) valpair is then (1,2,3,4), and moneyd (the dictionary containing key / valpair) is ('1':'a', '2':'b', etc)
# Then it prints the list, and asks the customer if they want to change a value to the list, asks for the value, and stores it alist

alist = ["a", "b", "c", "d", "e", "f"]
key = []
valpair = []
a = 1
b = '.'

for i in range(len(alist)):
	a_str = str(a)  # Converts the value stored in "a" to a string
	i_alist = alist[i]  # i_alist = element value of alist, so a = 1, b = 2, c = 3, etc
	key.append(a_str)  # Append the amount stored in "a" (a list of numbers starting at 1), to the list key
	valpair.append(i_alist)  # Append each element of list "alist"to list valpair, this is done for later, (a,b,c,etc)
	print(a_str + b, i_alist)  # Print the value in a_str (1,2,3, etc), followed by a ".", and the elements in i_alist (a,b,c) followed by a new line (1. a, 2. b, etc)
	a = a + 1  # Ups the amount stored in "a for every value stored in alist, so as to create a key that = (1,2,3,4,5,6)

print("key =", key)
print ("value pair =", valpair)


# Need to build a dictionary where a is the key, and valpair is the value pair (done)
# Ask customer to modify the value to the key (done)
# Clear the orginal list alist and replace it with the a new value pair list created by the user
# Continue on with the new values in alist

moneyd = dict(zip(key, valpair))  # takes the lists key and valpair, and stores them as a dictionary
print("dictionary".rstrip(), '=', moneyd)


# This needs to be in a loop

print("\nWhich value would you like to change, please type the number that corresponds to the value")
key_input = str(input("> "))

moneyd_key = moneyd[key_input]

print (key_input, "=".strip(), moneyd_key)

valchange = str(input("\nWhat is the value you would like to change it to?\n> "))


# modifying elements of a dictionary
moneyd[key_input] = valchange
print (key_input, f"is now \"{valchange}\"")
print(moneyd)
