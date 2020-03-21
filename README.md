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
- [x] Added terminal colors!    
- [ ] Functionalize code (make function calls within switch statements and loops)
- [ ] Give user ability to edit mistakes

----
### Long term goals
- [ ] Use the ncurses library to provide a graphical interface for the command line
- [ ] Add other functions outside of sum (avg, mode, median, etc)


**Current output _as of 03/21/2020_**

![Screenshot](https://github.com/StewAlexanderACC/checkbook_balancer.py/blob/master/3-21-ScreenShot.png)

**Output of the above (_as of 03/21/2020_) to _Checkbook.txt_** 
```
 > cat  Checkbook.txt
"+------------------+
| Org Bal: $200.00 |
+------------------+
|     -$150.00     |
|     -$15.00      |
|     -$23.34      |
|     -$23.24      |
|     $200.00      |
|     -$50.23      |
+------------------+"
Total = $138.19⏎  
```
