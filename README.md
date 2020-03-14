# Checkbook.py

A simple checkbook program that uses [poka-yoke](https://asq.org/quality-resources/mistake-proofing
) principles <br>

- [x] Assumes user wants to add another number until equal sign is typed (tells user this behavior up front)
- [x] Gives user the ability to quit with “q”
- [x] If list of debits / deposits is greater than 4, send each formatted amount to a new line
- [x] Gives user ability to save final results to a file
- [ ] Format as a CSV
- [ ] Functionalize code (make function calls within switch statements and loops)
- [ ] Give user ability to edit mistakes
- [ ] Running total?

----
### Long term goals
- [ ] Use the ncurses library to provide a graphical interface for the command line
- [ ] Add other functions outside of sum (avg, mode, median, etc)


**Current output _as of 03/14/2020**
```
> ./checkbook.py

This program very simply balances your checkbook
It will ask you for your orignal balance and any debits
- If you have a deposit, put a minus sign in front of the number

What is your orginal balance? > 6000

What is the first debit (if deposit put a -)?
> 400

Any more debit / deposits? Y/N
> y


(Use a "-" for deposits, "=" when done, or "q" to quit)
>   50
>   50
>   =

--------------------------------------------------------------

The numbers you entered are: ['$400.00', '$50.00', '$50.00']
A Total debit of:  $500.00


From what you entered:
$6,000.00 - $500.00 = $5,500.00

###################################################
Total remaining balance = $5,500.00
###################################################


Would you like to save this information Y/N?
> y
Saving to Checkbook.txt ...

Saved, quitting...
```
**Output of the above to _Checkbook.txt_** 
```
$6,000.00
----------
-$400.00
-$50.00
-$50.00
----------
Sum = $5,500.00
```
