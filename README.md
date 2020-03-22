# Checkbook.py

A simple checkbook program that uses [poka-yoke](https://asq.org/quality-resources/mistake-proofing
) principles <br>

Don't know Python? Start [here](https://www.pythoncheatsheet.org/) or [here](https://github.com/gto76/python-cheatsheet) 

**Requires**: <br>
PrettyTable and Termcolor, to install: <br>
- ```$ pip3 install prettytable```
- ```$ pip3 install termcolor```

<h3> How to run the program </h2>

- In any Linux or Mac environment by downloading "checkbook"
- Run the command ```chmod +x checkbook```
- Then start the program by ```$./checkbook```

<h3> Project Milestones and goals ...</h3>

- [x] Assumes user wants to add another number until equal sign is typed (tells user this behavior up front)
- [x] Gives user the ability to quit with “q”
- [x] If list of debits / deposits is greater than 4, send each formatted amount to a new line
- [x] Gives user ability to save final results to a file
- [x] Take data and print it using the "pretty table" library (looks better on screen, creates room for future development)<br>
    _See https://ptable.readthedocs.io/en/latest/tutorial.html_
- [x] Added colors! <br>
 _Unfortunately color ASCII sequences show up if you open the txt file with an editor, working on this_
- [x] Run the program by downloading the **checkbook** program, and typing ```$./checkbook``` in the folder it is located
   
----
### Long term goals
- [ ] Use the ncurses library to provide a graphical interface for the command line
- [ ] Add other functions outside of sum (avg, mode, median, etc)


**Current output _as of 03/22/2020_**

![Screenshot](https://github.com/StewAlexanderACC/checkbook_balancer.py/blob/master/Capt-3-22.png)

**Output of the above (_as of 03/22/2020_) to _Checkbook.txt_** 

 ```> cat  Checkbook.txt``` <br>
 
![Checkbook_output](https://github.com/StewAlexanderACC/checkbook_balancer.py/blob/master/chkbk-3-22.png)
