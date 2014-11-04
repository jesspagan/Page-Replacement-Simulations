# ----------------------------------------------------------------------------
# Assignment 03: Second Chance Page Replacement Algorithm
# University of Puerto Rico Rio Piedras Campus
# Department of Computer Science
# CCOM 4017: Operating System
# Student: Jessica Pagan Sanchez

# Description: Second Chance algorithm implements page removing the least use
# pages and gives more time in memory for recently used pages.
# The following code will:
#    - simulates the Second Chance algorithm
#    - returns the amounts of page faults that occurred 
# -----------------------------------------------------------------------------

import sys

# --- Main variables for the simulation --- #

f = open(sys.argv[2], 'r')		#open the file with the access requests
p = f.read().split() 			#read the file content and enter each request in an array
f.close()

N = int(sys.argv[1])				#number of physical memory pages
page_fault = 0 					#counter total page faults
m = [] 							#physical memory

# --- Looking for pages in memory and counting page faults --- #
for i in p:
	s = i.split(':')			#separating READ/WRITE from page number
	page = s[1]					#page in virtual machine

	# --- Verify if page already exist in memory --- #
	if page not in m:

		# --- If there's free memory space, insert the new one add the end --- #
		if len(m) < N:
			m.append(page)
			page_fault += 1
			# print 'NEW ' + page + ': ', m 			#debbuging

		# --- If not enough memory space, remove first page of the list and
		# --- add the new one at the end --- #
		else:
			m.pop(0)
			m.append(page)
			page_fault += 1
			# print 'NO MEM ' + page + ': ', m 		#debbuging

	# --- Move page to the end of the list --- #
	else:
		m.remove(page)
		m.append(page)
		# print 'EXISTS ' + page + ': ', m 				#debbuging

# --- Display information --- #
print 'Final state of memory: ', m
print 'Total page faults: ', page_fault