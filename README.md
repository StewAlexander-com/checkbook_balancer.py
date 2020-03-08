# Checkbook.py

A simple checkbook program that uses [poka-yoke](https://asq.org/quality-resources/mistake-proofing
) principles <br>

- [x] Instead assume user wants another number until equal sign is typed (tell user this behavior up front)
- [x] Give user the ability to quit with “q”
- [ ] Give user ability to save final results with “s”” to a .cvs  file
- [ ] Give user ability to edit mistakes 
- [ ] Running total?

----

## Current output _as of 03/08/2020_
```
home@mac-mini ~/Desktop> ./checkbook.py

This program very simply balances your checkbook
It will ask you for your orignal balance and any debits
- If you have a deposit, put a minus sign in front of the number

What is your orginal balance?  2100
What is the first debit (if deposit put a -)?  120

Any more debit / deposits? Y/N  y
(Use a "-" for deposits, "=" when done, or "q" to quit)

>   340
>   210
>   15
>   =

--------------------------------------------------------------

The numbers you entered are ['$120.00', '$340.00', '$210.00', '$15.00']
A Total debit of  $685.00


From what you entered:
$2,100.00 - $685.00 = $1,415.00

###################################################
Total remaining balance = $1,415.00
###################################################
```
