import sys
import re

genome_file = sys.argv[1]

dna_sequence = ""

with open(genome_file, "r") as f:
	for line in f.readlines():
		if not line[0] == ">":
			dna_sequence = dna_sequence + line
dna_sequence = dna_sequence.replace("\n", "")
dna_sequence = dna_sequence.upper()

pattern = ""

for i in sys.argv[2]
	if (i == "N"):
		pattern = pattern + "[A|C|T|G]"
	else:
		pattern = pattern + i

S = re.findall(pattern, dna_sequence)

for i in S:
	dna_sequence = dna_sequence.replace(i, "*")

fragments = dna_sequence.split("*")

for i in fragments:
	print("Fragment Length: ", len(i))
print("Number of fragments: ", len(fragments))
