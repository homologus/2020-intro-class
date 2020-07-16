f = open('/share/SARS/SARS-2020.fasta', 'r')
s = f.readlines()
finalstr = ''
p = {'TTT':'F','TTC':'F','TTA':'F','TTG':'F','CTT':'L','CTC':'L','CTA':'L','CTG':'L','ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A','TAT':'Y','TAC':'T','TAA':'','TAG':'','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E','TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
a = []
m = []
for h in range(1, len(s)):
	finalstr = finalstr + s[h].rstrip("\n")
for i in range(0, len(finalstr), 3):
        if ((len(finalstr[i:i+3])) == 3):
                a.append(p[finalstr[i:i+3]])
for j in range(0, len(a)):
        if (a[j] == "*"):
                m.append(j)
#print (m)
for k in range(0, len(m)-1):
        if ((m[k+1] - m[k])>= 100):
		z = a[m[k]:m[k+1]]
                print(''.join(a[m[k]:m[k+1]]))
def substring(string, start, end):
	return string[start:end]

