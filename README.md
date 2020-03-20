# Checkbook.py

A simple checkbook program that uses [poka-yoke](https://asq.org/quality-resources/mistake-proofing
) principles <br>

Don't know Python? Start [here](https://www.pythoncheatsheet.org/) or [here](https://github.com/gto76/python-cheatsheet) 

- [x] Assumes user wants to add another number until equal sign is typed (tells user this behavior up front)
- [x] Gives user the ability to quit with “q”
- [x] If list of debits / deposits is greater than 4, send each formatted amount to a new line
- [x] Gives user ability to save final results to a file
- [x] Take data and print it using the "pretty table" library (looks better on screen, creates room for future development)<br>
    _See https://ptable.readthedocs.io/en/latest/tutorial.html_
- [ ] Functionalize code (make function calls within switch statements and loops)
- [ ] Give user ability to edit mistakes

----
### Long term goals
- [ ] Use the ncurses library to provide a graphical interface for the command line
- [ ] Add other functions outside of sum (avg, mode, median, etc)


**Current output _as of 03/20/2020**
```
> ./checkbook.py

This program very simply balances your checkbook
It will ask you for your orignal balance and any debits
- If you have a deposit, put a minus sign in front of the number

What is your orginal balance? > 500

What is the first debit (if deposit put a -)? 
> 100

Any more debit / deposits? Y/N 
> y


(Use a "-" for deposits, "=" when done, or "q" to quit)
>   50
>   50
>   100
>   =

--------------------------------------------------------------

The numbers you entered are: ['$100.00', '$50.00', '$50.00', '$100.00']
A Total debit of:  $300.00


From what you entered:
$500.00 - $300.00 = $200.00

###################################################
Total remaining balance = $200.00
###################################################


Would you like to save this information Y/N?
> y

-- Removed previous Checkbook.txt --

Saving data to Checkbook.txt ...

Saved, quitting...
support@support-VirtualBox ~/Desktop> 

```
**Output of the above (_as of 03/20/2020_) to _Checkbook.txt_** 
```
> cat Checkbook.txt 
"+------------------+
| Org Bal: $500.00 |
+------------------+
|     -$100.00     |
|     -$50.00      |
|     -$50.00      |
|     -$100.00     |
+------------------+"
Total = $200.00           
```
