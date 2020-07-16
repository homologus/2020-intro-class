f = open("/share/SARS/SARS-2020.fasta")
line = f.readlines()
strand = ""
for i in range (1, len(line)):
	for j in range(len(line[i]) - 1):
		strand = strand + line[i][j]
proteins = {'TTT' : 'F', 'TTC' : 'F', 'TTA' : 'L', 'TTG' : 'L', 'CTT' : 'L', 'CTC' : 'L', 'CTA' : 'L', 'CTG' : 'L', 'ATT' : 'I', 'ATC' : 'I', 'ATA' : 'I', 'ATG' : 'M', 'GTT' : 'V', 'GTC' : 'V', 'GTA': 'V', 'GTG': 'V', 'TCT' : 'S', 'TCC' : 'S', 'TCA': 'S', 'TCG' : 'S', 'CCT' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'ACT' : 'T', 'ACC' : 'T', 'ACA': 'T', 'ACG' : 'T', 'GCT' : 'A', 'GCC' : 'A', 'GCA': 'A', 'GCG' : 'A', 'TAT': 'Y', 'TAC' : 'Y', 'TAA' : '*', 'TAG': '*', 'CAT' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'AAT' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K', 'GAT' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E', 'TGT' : 'C', 'TGC' : 'C', 'TGA' : '*', 'TGG' : 'W', 'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG': 'R', 'AGT' : 'S', 'AGC' : 'S', 'AGA' : 'R', 'AGG' : 'R', 'GGT' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G' }
for i in range(0 , 3):
	extra = (len(strand) - i) % 3
	protseq = ""
	for j in range(i, len(strand) - extra, 3):
		protseq = protseq + proteins[strand[j:j+3]]
	newseq = ""
	count = 0
	longseq = 0
	for j in range(len(protseq)):
		if(protseq[j] != '*'):
			count = count + 1
		else:
			if(count > 100):
				longseq = longseq + 1
				for k in range(j - count, j + 1):
					newseq = newseq + protseq[k]
				print("from " + str(3 * (j - count) + i) + " to " + str(3 * j + i + 2))
			count = 0
	print("Reading frame " + str(i + 1) + ":" + newseq)
	print("Number of sequences greater than 100 amino acids: " + str(longseq))

