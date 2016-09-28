#!/usr/bin/env python

# usage: pyhton match_index2reads_fastq.py reads.fastq index.fastq

import sys
reads = sys.argv[1]
index = sys.argv[2]
all_readIDs = set()

# The code below is written to only ever read the first row:
with open(reads, "r") as read_file:
	while True:
		try:
			line1 = next(read_file)
			if line1.startswith("@HWI"): all_readIDs.add(line1)
			next(read_file) # We walk through the
			next(read_file) # next 3 lines but don't
			next(read_file) # save the data anywhere. 
		except StopIteration:
			break
# This is to test the content of the list
if not all_readIDs: print "List is Empty"
else:
	for idx,item in enumerate(all_readIDs):
		print item
		if idx == 10: break

# The code below will not skip any rows and write all 4 rows to a file if the ID line in the ID set:
with open(index, "r") as index_file, open("filtered_index.fastq", "w") as filtered_file:
	while True:
		try:
			line1 = next(index_file)
			line2 = next(index_file)
			line3 = next(index_file)
			line4 = next(index_file)
		except StopIteration:
			break
		if line1 in all_readIDs:
			filtered_file.write(line1)
			filtered_file.write(line2)
			filtered_file.write(line3)
			filtered_file.write(line4)
print "All done!"
