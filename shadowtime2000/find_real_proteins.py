import sys

converting_dictionary  = {"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A","CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R","AAT":"N", "AAC":"N","GAT":"D", "GAC":"D","TGT":"C", "TGC":"C","CAA":"Q", "CAG":"Q","GAA":"E", "GAG":"E","GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G","CAT":"H", "CAC":"H","ATT":"I", "ATC":"I", "ATA":"I","ATG":"M","TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L","AAA":"K", "AAG":"K","TTT":"F", "TTC":"F","CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P","TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S","ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T","TGG":"W","TAT":"Y", "TAC":"Y","GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V","TAA":"*", "TGA":"*", "TAG":"*"}

file = sys.argv[1]

real_protein_length = int(sys.argv[2])

reading_frame = int(sys.argv[3])

sequence_file = sys.argv[4]

errors = 0

dna_sequence = ""

with open(file, "r") as f:
	for line in f.readlines():
		if not line[0] == ">":
			dna_sequence = dna_sequence + line

if not(len(dna_sequence) % 3 == 0):
	print("Invalid DNA Sequence! Is not appropriate length!")

dna_sequence = dna_sequence.replace("\n", "")

amino_acids = ""

for i in range(reading_frame, len(dna_sequence), 3):
	try:
		amino_acids = amino_acids + converting_dictionary[dna_sequence[i:i+3]]
	except KeyError:
		print("Breaking because end of DNA sequence found")
		break
amino_acid_array = amino_acids.split("*")

new_amino_acid_array = []

for i in amino_acid_array:
	if (len(i) > real_protein_length):
		new_amino_acid_array.append({"starting_point": amino_acids.find(i), "length": len(i)})
		with open(sequence_file, "a+") as f:
			f.write(i + "\n")
for i in new_amino_acid_array:
	print("Start: ", i["starting_point"])
	print("Length: ", i["length"])
	print("End: ", i["starting_point"] + (i["length"]*3))
