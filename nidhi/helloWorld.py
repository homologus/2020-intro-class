f = open('/share/SARS/SARS-2020.fasta', 'r')
lines = f.readlines()
count_A = 0
count_C = 0
count_T = 0
count_G = 0
finalstr = ''
for k in range(1, len(lines)):
	finalstr = finalstr + lines[k].rstrip ("\n")
for i in range(0, len(finalstr)):
	if (finalstr[i]=='A'):
		count_A = count_A + 1
	if (finalstr[i]=='C'):
		count_C = count_C + 1
	if (finalstr[i]=='T'):
		count_T = count_T + 1
	if (finalstr[i]=='G'):
		count_G = count_G + 1
print (count_A, count_C, count_T, count_G)
print (len(finalstr))

