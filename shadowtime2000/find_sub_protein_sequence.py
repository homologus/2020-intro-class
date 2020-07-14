import sys

genome_file = sys.argv[1]

reading_frame = int(sys.argv[2])

start = int(sys.argv[3])

end = int(sys.argv[4])

dna_sequence = ""

with open(genome_file, "r") as f:
	for line in f.readlines():
		if not line[0] == ">":
			dna_sequence = dna_sequence + line
dna_sequence = dna_sequence.replace("\n", "")


converting_dictionary  = {"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A","CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R","AAT":"N", "AAC":"N","GAT":"D", "GAC":"D","TGT":"C", "TGC":"C","CAA":"Q", "CAG":"Q","GAA":"E", "GAG":"E","GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G","CAT":"H", "CAC":"H","ATT":"I", "ATC":"I", "ATA":"I","ATG":"M","TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L","AAA":"K", "AAG":"K","TTT":"F", "TTC":"F","CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P","TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S","ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T","TGG":"W","TAT":"Y", "TAC":"Y","GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V","TAA":"*", "TGA":"*", "TAG":"*"}

amino_acids = ""

for i in range(reading_frame, len(dna_sequence), 3):
	try:
		amino_acids = amino_acids + converting_dictionary[dna_sequence[i:i+3]]
	except KeyError:
		print("Breaking because end of DNA Sequence found")
		break

print(amino_acids[start:end])
