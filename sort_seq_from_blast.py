#!/usr/bin/python

##This script select sequences that has 100% BLAST in a 
##blast result file put them in another file

input_file = open("blast_out", "r")
all_BLAST_lines = input_file.readlines()
input_file.close()

thingswewant = []
for i, line in enumerate(all_BLAST_lines):
	if line[0] != "#" and line != "":
		temp = line.split()
		queryID = temp[0]
		subjectID = temp[1]
		ident = float(temp[2])

		if ident >= 100:
			thingswewant.append(subjectID)

raw_reads_file = open("raw_reads.fna", "r")
all_raw_seqs = raw_reads_file.readlines()
raw_reads_file.close()

output = open("all_100.fasta", "w")
for i, line in enumerate(all_raw_seqs):
	if line[0] == ">":
		temp = line[1:].split()
		targetID = temp[0]

		if targetID in thingswewant:
			output.write(line + all_raw_seqs[i+1])

output.close()
