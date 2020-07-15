import sys

restriction_site1 = "GAC"
restriction_site2 = "GTC"

restriction_site_reverse1 = "CTG"
restriction_site_reverse2 = "CAG"

genome_file = sys.argv[1]

dna_sequence = ""

with open(genome_file, "r") as f:
	for line in f.readlines():
		if not line[0] == ">":
			dna_sequence = dna_sequence + line
dna_sequence = dna_sequence.replace("\n", "")

for i in range(0, len(dna_sequence), 11):
	if (dna_sequence[i:i+3] == restriction_site1 and dna_sequence[i+8:i+11] == restriction_site2):
		dna_sequence = dna_sequence.replace(dna_sequence[i:i+11], "*")

fragments = dna_sequence.split("*")

for i in fragments:
	print("Fragment Length: ", len(i))


