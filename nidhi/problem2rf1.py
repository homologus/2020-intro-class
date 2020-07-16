f = open('/share/SARS/SARS-2020.fasta', 'r')
s = f.readlines()
x = 0
finalstr = ''
p ={'TTT':'F','TTC':'F','TTA':'F','TTG':'F','CTT':'L','CTC':'L','CTA':'L','CTG':'L','ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A','TAT':'Y','TAC':'T','TAA':'','TAG':'','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E','TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
for j in range(1, len(s)):
        finalstr = finalstr + s[j].rstrip("\n")
a = []
m = []
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
print(x)
print(m)
