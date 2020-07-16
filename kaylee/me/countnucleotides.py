f = open("/share/SARS/SARS-2020.fasta")
line = f.readlines()
count = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}
for i in range (1, len(line)):
	for j in range(0, len(line[i]) - 1):
		count[line[i][j]] = count[line[i][j]] + 1
gccontent = (count['G'] + count['C']) / (count['A'] + count['T'] + count['G'] + count['C']) * 100
print("Number of Adenine: " + str(count['A']) + " Number of Thymine: " + str(count['T']) + " Number of Guanine: " + str(count['G']) + " Number of Cytosine: " + str(count['C']) + " GC-content: " + str(gccontent) + "%")
