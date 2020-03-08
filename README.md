# Checkbook.py

A simple checkbook program that uses [poka-yoke](https://asq.org/quality-resources/mistake-proofing
) principles <br>

- [x] Instead assume user wants another number until equal sign is typed (tell user this behavior up front)
- [x] Give user the ability to quit with “q”
- [x] If list of numbers is greater than 3, send each to a new line
- [ ] Give user ability to save final results with “s”” to a .cvs  file
- [ ] Give user ability to edit mistakes 
- [ ] Running total?

----

**Current output _as of 03/08/202_  if debits / deposits greater than 4:**
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

