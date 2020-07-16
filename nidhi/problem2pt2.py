f = open('/share/SARS/SARS-2020.fasta', 'r')
s = f.readlines()
x = 0
y = 0
z = 0
finalstr = ''
p ={'TTT':'F','TTC':'F','TTA':'F','TTG':'F','CTT':'L','CTC':'L','CTA':'L','CTG':'L','ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A','TAT':'Y','TAC':'T','TAA':'','TAG':'','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E','TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
for j in range(1, len(s)):
	finalstr = finalstr + s[j].rstrip("\n")
a = []
b = []
c = []
m = []
l = []
q = []
for i in range(0, len(finalstr), 3):
	if ((len(finalstr[i:i+3])) == 3):
		a.append(p[finalstr[i:i+3]])
for i in range(0, len(a)):
	if (a[i] == "*"):
		m.append(i)
for k in range(0, len(m)-1):
	if ((m[k+1] - m[k])>= 100):
		print(m[k])
		x = x+1
print (x)
for i in range(1, len(finalstr), 3):
        if ((len(finalstr[i:i+3])) == 3):
                b.append(p[finalstr[i:i+3]])
for i in range(0, len(b)):
        if (b[i] == "*"):
                l.append(i)
for k in range(0, len(l)-1):
        if ((l[k+1] - l[k])>= 100):
                print(l[k])
                y = y+1
print (y)
for i in range(2, len(finalstr), 3):
        if ((len(finalstr[i:i+3])) == 3):
                c.append(p[finalstr[i:i+3]])
for i in range(0, len(c)):
        if (c[i] == "*"):
                q.append(i)
for k in range(0, len(q)-1):
        if ((q[k+1] - q[k])>= 100):
                print(q[k])
                z = z+1
print (z)
print (''.join(a))

