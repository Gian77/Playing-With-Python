#!/usr/bin/python

#usage $: python split_fastq_buIDs.py ID1 ID2 ID3 ...
#remember to check sample header in the fastq file and make requred changes at line 20

import sys

target_ids = sys.argv[1:]
print target_ids


imputfile = open("seqs.fastq", "r")
all_lines = imputfile.readlines()
imputfile.close()


all_samples ={}
for i, line in enumerate(all_lines):
	temp = line.split("_")
	if line.startswith("@sam") and len(temp) >1:
		sampleID = temp[0][1:]
		uniqueID = temp[1]
		if sampleID not in all_samples.keys():
			all_samples[sampleID]={}
		all_samples[sampleID][uniqueID]=''.join(all_lines[i:i+4])

for each_target in target_ids:
	output = open(each_target+".fastq", "w")
	for each_read in all_samples[each_target]:
		output.write(all_samples[each_target][each_read])
	output.close()
