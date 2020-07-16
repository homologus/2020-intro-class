import sys
import re

restriction_site1 = "GAC"
restriction_site2 = "GTC"

genome_file = sys.argv[1]

dna_sequence = ""

with open(genome_file, "r") as f:
	for line in f.readlines():
		if not line[0] == ">":
			dna_sequence = dna_sequence + line
dna_sequence = dna_sequence.replace("\n", "")
dna_sequence = dna_sequence.upper()

S = re.findall("GAC[A|G|C|T][A|G|C|T][A|G|C|T][A|G|C|T][A|G|C|T]GTC", dna_sequence)

for i in S:
	dna_sequence = dna_sequence.replace(i, "*")

fragments = dna_sequence.split("*")

for i in fragments:
	print("Fragment Length: ", len(i))
print("Number of fragments: ", len(fragments))
