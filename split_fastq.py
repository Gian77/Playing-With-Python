#!/usr/bin/python

##This script simply split a fastq file according header's IDs

imputfile = open("seqs.fastq", "r")
all_lines = imputfile.readlines()
imputfile.close()

all_samples ={}
for i, line in enumerate(all_lines):
	temp = line.split("_")
	if line[0] == "@" and len(temp) >1:
		sampleID = temp[0][1:]
		uniqueID = temp[1]
		if sampleID not in all_samples.keys():
			all_samples[sampleID]={}
		all_samples[sampleID][uniqueID]=''.join(all_lines[i:i+4])

for each_sample in all_samples.keys():
	output = open(each_sample+".fastq", "w")
	for each_read in all_samples[each_sample]:
		output.write(all_samples[each_sample][each_read])
	output.close()


	

