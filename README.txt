-----------------------------
Contact Information
-----------------------------
Author:			Jessica Pagan Sanchez
Student Number:	801-06-5651
Email:			jessica.pagan3@upr.edu
Project:		CCOM4017 - Homework 3

-----------------------------
Description
-----------------------------
The purpose of this assigment is to simulate three algorithms that are use for Memory Management.
Their are Optimal Page Replacement, Second Chance Page Replacement 
and WSClock (Working Set with Clock) Page Replacement.

The programming language use is Python, that runs in Unix Terminal. For others, please install 
a python interpreter.
https://www.python.org/download

---------------------------------------
How to use it and execute the process
---------------------------------------
From the terminal:

The three simulations can be use independently from each other.

1. Open the terminal

3a. To open Optimal or Second Chance simulations, enter the following command:

	 python <filename.py> <memory_capacity> <requested_accesses.txt>

      Ex. python optimal.py 10 accessreq.txt

3b. To open WSClock simulation, enter the following command:

    python <filename.py> <memory_capacity> <tau> <requested_accesses.txt>

      Ex. python wsclock.py 10 5 accessreq.txt

4. After this, all simulation will start reading the access reuqestes in sequencial order.

6. It will do the following instructions based in their individual algorithms and print the total fault.

7. The should have the same amount of total fault for the same amount of memory space.

---------------------------------------
Who helped
---------------------------------------
Instructor: 			Jose Ortiz
Email: 					cheo@hpcf.upr.edu

Graduate Student:		Rafael Esparra
Email: 					rafael.esparra1@upr.edu

