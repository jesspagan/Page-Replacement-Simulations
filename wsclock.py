# ----------------------------------------------------------------------------
# Assignment 03: WSClock Page Replacement Algorithm
# University of Puerto Rico Rio Piedras Campus
# Department of Computer Science
# CCOM 4017: Operating System
# Student: Jessica Pagan Sanchez

# Description: WSClock algorithm implements clock and working set algorithms
# to find a suitable cancidated to located the new request
# The following code will:
#    - simulates the WSClock algorithm
#    - returns the amounts of page faults that occurred 
# -----------------------------------------------------------------------------

import sys

# --- Main variables for the simulation --- #
f = open(sys.argv[3], 'r')		#open the file with the access requests
p = f.read().split() 			#read the file content and enter each request in an array
f.close()

N = int(sys.argv[1])			#number of physical memory pages
page_fault = 0 					#counter total page faults
m = [] 							#physical memory
index = 0						#points to the next page to be verify
tau = int(sys.argv[2]) 			#use to determine if page lived too long in memory
clock = 0


# --- Class that define the information of each page --- #
class Page:
	def __init__(self, number, last_use, ref_bit, modified):
		self.n = number 	#page number
		self.t = last_use	#time of last use
		self.r = ref_bit	#reference bit
		self.m = modified	#READ/WRITE mode

# --- Taking number of pages and adding on a new list --- #
pages = []
for i in p:
	s = i.split(':')	#separating READ/WRITE from page number
	if s[0] == 'W':
		s[0] = 1
	else:
		s[0] = 0
	pages.append(s)		#page in virtual machine

# --- Looking for pages in memory and counting page faults --- #
for i in pages:
	clock += 1

	# --- Verify if page already exist in memory --- #
	found = False
	for j in m:
		if i[1] == j.n:
			found = True
			j.r = 1
			j.t = clock

		# debbuging
			# mem = []
			# for n in m:
			# 	mem.append([n.n,n.r,n.t])
			# print 'UPDATED:', i, 'MEM:', mem

	# --- If not in memory, check if there's free memory space
	# --- and insert the new one add the end --- #
	if found == False:
		if len(m) < N:
			m.append(Page(i[1], clock, 1, i[0]))
			page_fault += 1
			index = (index + 1) % N
			found = True

		# debbuging
		# 	mem = []
		# 	for n in m:
		# 		mem.append([n.n,n.r,n.t])
		# 	print 'NEW:', i, 'MEM:', mem

	# --- If not enough memory space, check which page in memory is not referenced --- #
	if found == False:

		# if page is referenced, unreference it
		for j in range(N):

			if m[index].r == 1:
				m[index].r = 0
				index = (index + 1) % N

			# if page is unreferenced, check if age is bigger than tau
			elif m[index].r == 0:
				age = clock - m[index].t

				if age > tau:
					print i
					m[index] = Page(i[1], clock, 1, i[0])
					index = (index + 1) % N
					found = True
					page_fault += 1

				# debbuging
					# mem = []
					# for n in m:
					# 	mem.append([n.n,n.r,n.t])
					# print 'NON REF:', i, 'MEM:', mem

				break

	# --- If all pages are referenced, find the oldest one --- #				
	if found == False:
		for j in range(N):
			if clock - m[index].t == N:
				m[index] = Page(i[1], clock, 1, i[0])
				index = (index + 1) % N
				found = True
				page_fault += 1
				
			# # debbuging
			# 	mem = []
			# 	for n in m:
			# 		mem.append([n.n,n.r,n.t])
			# 	print 'OLDEST:', i, 'MEM:', mem

# --- Display information --- #
mem = []
for n in m:
	mem.append(n.n)

print 'Final state of memory: ', mem
print 'Total page faults: ', page_fault
