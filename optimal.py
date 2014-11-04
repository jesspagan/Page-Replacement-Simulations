# ----------------------------------------------------------------------------
# Assignment 03: Optimal Page Replacement Algorithm
# University of Puerto Rico Rio Piedras Campus
# Department of Computer Science
# CCOM 4017: Operating System
# Student: Jessica Pagan Sanchez

# Description: Optimal algorithm implements page removing in full used memory
# determinating which future pages will be use less.
# The following code will:
#    - simulates the Optimal algorithm
#    - returns the amounts of page faults that occurred 
# -----------------------------------------------------------------------------

import sys

# --- Main variables for the simulation --- #
print sys.argv

f = open(sys.argv[2], 'r')						#open the file with the access requests
p = f.read().split() 							#read the file content and enter each request in an array
f.close()

N = int(sys.argv[1])							#number of physical memory pages
page_fault = 0 									#counter total page faults
m = [] 											#physical memory

# --- Taking number of pages and adding on a new list --- #
pages = []
for i in p:
	s = i.split(':')							#separating READ/WRITE from page number	
	pages.append(s[1])							#page in virtual machine

# --- Removing pages while the have been verify -- #
while len(pages) != 0:

	# --- Verify if page already exist in memory --- #
	if pages[0] in m:
		pages.pop(0)

	else:
		# --- If there's free memory space, insert the new one add the end --- #
		if len(m) < N:
			m.append(pages[0])		
			pages.pop(0)
			page_fault += 1
			# print 'NEW ' + m[len(m)-1] + ': ', m 		#debbuging

		# --- Finding the page with less use in memory --- #
		else:
			less_use = 0;						#identify which page will be remove
			time_use = len(pages) - 1;			#amount of time remaing for use

			for i in m:
				total = 0;						#count for total future use in memory of i page
				last_pos = 0;					#how far is the last use of the page

				for j in pages:
					if i == j:
						total += 1

				# --- If page in memory will not be use again, remove it --- #
				if total == 0:
					less_use = i
					break

				# --- If page will be use, check if will be use less than others --- #
				elif total < time_use or (total == time_use and pages.index(i) > pages.index(less_use)): 
					time_use = total
					less_use = i

			# --- Removing the least use page in memory --- #
			m.pop(m.index(less_use))
			m.append(pages[0])
			pages.pop(0)
			page_fault += 1
			# print 'least use ' + less_use + ': ', m 	#debbuging

# --- Display information --- #
print 'Final state of memory: ', m
print 'Total page faults: ', page_fault
