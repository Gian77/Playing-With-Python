#!/usr/bin/python

## 454 sequence file example 
##
## >H6S4ZXQ05F9IEN length=56 xy=2451_2269 region=5 run=R_2013_03_27_03_22_35_
## ACAGTCGTGCCTTGGTCATTTAGAGGAAGTAACCTGGGCATATCAATAAGCGGAGG
## >H6S4ZXQ05GD7DU length=56 xy=2505_0080 region=5 run=R_2013_03_27_03_22_35_
## TGTCACACGACTTGGTCATTTAGAGGAAGTAACCTGGGCATATCAATAAGCGGAGG
## >H6S4ZXQ05FXZMR length=54 xy=2320_1297 region=5 run=R_2013_03_27_03_22_35_
##
##


input_file = open("mapping_file.txt", "r")
all_BARCODE_lines = input_file.readlines()
input_file.close()

thingswewant = []
for i, line in enumerate(all_BARCODE_lines):
	if line[0] != "#":
		temp = line.split()
		SampleID = temp[0]
		BarcodeSequence = temp[1]
			thingswewant.append(BarcodeSequence)

raw_reads_file = open("H6S4ZXQ05.fna", "r")
all_raw_seqs = H6S4ZXQ05_file.readlines()
raw_reads_file.close()

output = open("allOTUs_100.fna", "w")

for i, line in enumerate(all_raw_seqs):
	if line[0] == ">":
		temp = line[1:].split()
		temp = line 
		
		targetID = temp[0]

		if BarcodeSequence in thingswewant:
			output.write(line + all_raw_seqs[i+1])

output.close()



