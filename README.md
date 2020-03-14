# Checkbook.py

A simple checkbook program that uses [poka-yoke](https://asq.org/quality-resources/mistake-proofing
) principles <br>

- [x] Assumes user wants to add another number until equal sign is typed (tells user this behavior up front)
- [x] Gives user the ability to quit with “q”
- [x] If list of debits / deposits is greater than 4, send each formatted amount to a new line
- [x] Gives user ability to save final results to a file
- [ ] Functionalize code (make function calls within switch statements and loops)
- [ ] Give user ability to edit mistakes

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

What is your orginal balance? > 340.54

What is the first debit (if deposit put a -)? 
> 12.23

Any more debit / deposits? Y/N 
> y


(Use a "-" for deposits, "=" when done, or "q" to quit)
>   1.23
>   34.56
>   -120
>   -86.23
>   =

--------------------------------------------------------------

The numbers you entered are:

$12.23
$1.23
$34.56
-$120.00
-$86.23
---------
A total deposit of:  $158.21


From what you entered:
$340.54 + $158.21 = $498.75

###################################################
Total remaining balance = $498.75
###################################################


Would you like to save this information Y/N?
> y

-- Removed previous Checkbook.txt --

Saving data to Checkbook.txt ...

Saved, quitting...
```
**Output of the above to _Checkbook.txt_** 
```
Orginal Bal: 340.54
----------
-$12.23
-$1.23
-$34.56
$120.00
$86.23
----------
Total = $498.75
```
