f = open('/share/SARS/SARS-2020.fasta', 'r')
s = f.readlines()
finalstr = ''
for p in range(1, len(s)):
        finalstr = finalstr + s[p].rstrip("\n")
a = []
b = []
c = []
total100aa = 0
p = {'TTT':'F','TTC':'F','TTA':'F','TTG':'F','CTT':'L','CTC':'L','CTA':'L','CTG':'L','ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A','TAT':'Y','TAC':'T','TAA':'*','TAG':'*','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E','TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
for i in range(0, len(finalstr), 3):
        if ((len(finalstr[i:i+3])) == 3):
                a.append(p[finalstr[i:i+3]])
a = ''.join(a)
for i in range(0, len(a)-1):
	if (a[i] == "*"):
		for j in range(i+1, len(a)-1):
			if (a[j] == "*"):
				if ((j-i)>=100):
					print (''.join(a[i:j]))
					print (j-i)
					print ("i = " + str(i) + "," + "j = " + str(j))
					total100aa = total100aa + 1
				break
print ("-------------" + str(total100aa))
for i in range(1, len(finalstr), 3):
        if ((len(finalstr[i:i+3]))==3):
                b.append(p[finalstr[i:i+3]])

for i in range(0, len(b)-1):
        if (b[i] == "*"):
                for j in range(i+1, len(b)-1):
                        if (b[j] == "*"):
                                if ((j-i)>=100):
                                        print (''.join(b[i:j]))
                                        print (j-i)
                                        print ("i = " + str(i) + "," + "j = " + str(j))
                                        total100aa = total100aa + 1
                                break
print ("-------------" + str(total100aa))
#print (''.join(b))
for i in range(2, len(finalstr), 3):
        if ((len(finalstr[i:i+3]))==3):
                c.append(p[finalstr[i:i+3]])

for i in range(0, len(c)-1):
        if (c[i] == "*"):
                for j in range(i+1, len(c)-1):
                        if (c[j] == "*"):
                                if ((j-i)>=100):
                                        print (''.join(c[i:j]))
                                        print (j-i)
                                        print ("i = " + str(i) + "," + "j = " + str(j))
                                        total100aa = total100aa + 1
                                break
print ("-------------" + str(total100aa))
#print (''.join(c))
