# Checkbook_balancer.py

Simple Python script to balance one's checkbook

-----

## Project goals

03/07/2020 - </br>
At  the moment the script keeps asking you for another number, annoying and not [poka-yoke](https://asq.org/quality-resources/mistake-proofing)</br>
- [x] Instead assume user wants another number until equal sign is typed (tell user this behavior up front)
- [ ] Give user the ability to quit with “q”
- [ ] Give user ability to save final results with “s”
- [ ] Give user ability to edit mistakes 
- [ ] Running total?
---
Output _as of 03/07/2020_:
```
home@mac-mini ~/Desktop> ./checkbook.py

This program very simply balances your checkbook
It will ask you for your orignal balance and any debits
If you have a deposit, add a minus sign in front of the number

What is your orginal balance?  5400
What is the first debit (if deposit put a -)?  200

Any more debit / deposits? Y/N  y
(Use a "-" for deposit, or "=" when finished)

>   34
>   25
>   15
>   -8
>   =

--------------------------------------------------------------

The numbers you entered are ['$200.00', '$34.00', '$25.00', '$15.00', '-$8.00']
A Total debit of  $266.00


From what you entered:
$5,400.00 - $266.00 = $5,134.00

###################################################
Total remaining balance = $5,134.00
###################################################
```
