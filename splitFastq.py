#!/usr/bin/python

# to Split an Illumina Reads fastq by Header Name
# Make sure you change R1 to R2 if you are splitting reverse reads
# please see line 27
# usage: python split_fast.py inputfile.fastq

import sys
fastqfile = sys.argv[1]

imputfile = open(fastqfile, "r")
all_lines = imputfile.readlines()
imputfile.close()

all_samples ={}
for i, line in enumerate(all_lines):
	temp = line.split("_")
	if line.startswith("@") and len(temp) >1:
		sampleID = temp[0][1:]
		temp2 = temp[1].split()
		uniqueID = temp2[0]
		if sampleID not in all_samples.keys():
			all_samples[sampleID]={}
		all_samples[sampleID][uniqueID]=''.join(all_lines[i:i+4])

for each_sample in all_samples.keys():
	output = open(each_sample+"R2"+".fastq", "w") ## carefull here to selct the reads you want
	for each_read in all_samples[each_sample]:
		output.write(all_samples[each_sample][each_read])
	output.close()

