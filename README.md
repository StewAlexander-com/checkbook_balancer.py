# Checkbook.py

A simple checkbook program that uses [poka-yoke](https://asq.org/quality-resources/mistake-proofing
) principles <br>

- [x] Assume user wants another number until equal sign is typed (tell user this behavior up front)
- [x] Give user the ability to quit with “q”
- [x] If list of debits / deposits is greater than 4, send each formatted amount to a new line
- [ ] Give user ability to save final results with “s” to a CSV  file
- [ ] Functionalize code (make function calls within switch statements and loops)
- [ ] Give user ability to edit mistakes
- [ ] Running total?

----
### Long term goals
- [] Use the ncurses library to provide a graphical interface for the command line
- [] Add other functions outside of sum (avg, mode, median, etc)


**Current output _as of 03/08/2020_  if debits / deposits greater than 4:**
```
> ./checkbook.py

This program very simply balances your checkbook
It will ask you for your orignal balance and any debits
- If you have a deposit, put a minus sign in front of the number

What is your orginal balance? > 3400

What is the first debit (if deposit put a -)?
> 220.26

Any more debit / deposits? Y/N
> y

(Use a "-" for deposits, "=" when done, or "q" to quit)
>   3400
>   -7600
>   210
>   34
>   2
>   =

--------------------------------------------------------------

The numbers you entered are:

$220.26
$3,400.00
-$7,600.00
$210.00
$34.00
$2.00
---------
A total deposit of:  $3,733.74


From what you entered:
$3,400.00 + $3,733.74 = $7,133.74

###################################################
Total remaining balance = $7,133.74
###################################################```
```
---

**Current output _as of 03/08/2020_  if debits / deposits is 4 or less:**
```
> ./checkbook.py

This program very simply balances your checkbook
It will ask you for your orignal balance and any debits
- If you have a deposit, put a minus sign in front of the number

What is your orginal balance? > 3400

What is the first debit (if deposit put a -)?
> 12

Any more debit / deposits? Y/N
> y

(Use a "-" for deposits, "=" when done, or "q" to quit)
>   210
>   2
>   =

--------------------------------------------------------------

The numbers you entered are: ['$12.00', '$210.00', '$2.00']
A Total debit of:  $224.00


From what you entered:
$3,400.00 - $224.00 = $3,176.00

###################################################
Total remaining balance = $3,176.00
###################################################
```
