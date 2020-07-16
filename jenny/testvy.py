f=open('/share/SARS/SARS-2020.fasta','r')
x=f.readlines()[1:]
#x = ''.join (x[1:len(x)+1])
#x = x.replace ('\n','')
#print(len(x))

#print(x[1])

#strip \n characters
for i in range (0,len(x),1):
       x[i]=x[i].rstrip('\n')

#Join lists into single string
xLong=""
for i in x:
        xLong += str(i)


#print(xLong)
#print(len(xLong))

#dictionary
CodonsAndAminos = {
  'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
  'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
  'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
  'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
  'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
  'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
  'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
  'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
  'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*',
  'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
  'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
  'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
  'TGT':'C','TGC':'C','TGA':'*','TGG':'W',
  'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
  'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
  'GGT':'G','GGC':'G','GGA':'G','GGG':'G'
}                                                                                          
 #translate each to amino
protein = ""
aminoCount=0
protein100Count1=0
protein100Count2=0
protein100Count3=0
#First reading frame
for i in range (0,len(xLong),3):
	codon= xLong[i:i +3]
	if len(codon)==3:
		protein += CodonsAndAminos[codon]
for i in range (len(protein)):
	aminoCount=aminoCount+1
	if protein[i]=='*':
		if aminoCount>100:
			protein100Count1=protein100Count1+1
		aminoCount=0
aminoCount=0

protein = ""
for i in range (1,len(xLong)-2,3):
        codon= xLong[i:i +3]
        if len(codon)==3:
                protein += CodonsAndAminos[codon]

for i in range (len(protein)):
        aminoCount=aminoCount+1
        if protein[i]=='*':
                if aminoCount>100:
                        protein100Count2=protein100Count2+1
                aminoCount=0
aminoCount=0

protein = ""
for i in range (2,len(xLong)-1,3):
        codon= xLong[i:i +3]
        if len(codon)==3:
                protein += CodonsAndAminos[codon]
for i in range (len(protein)):
        aminoCount=aminoCount+1
        if protein[i]=='*':
                if aminoCount>100:
                        protein100Count3=protein100Count3+1
                aminoCount=0

print (protein100Count1)
print (protein100Count2)
print (protein100Count3)
print ("Total:",protein100Count1+protein100Count2+protein100Count3)
