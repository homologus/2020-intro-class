#fileVar = open('/share/SARS/SARS-2020.fasta','r')
#fileVar = open('/share/SARS/covid-patient-CA.fasta','r')
fileVar = open('/share/SARS/SARS-urbani.fasta','r')
#fileVar = open('/share/SARS/pangolin-cov.fasta','r')

#with open ('SARS-Genome') as fileVar:
#	variable = fileVar.read ()
#DNA = variable.replace('\n','')
variable = fileVar.readlines ()
DNA = ''.join (variable[1:len(variable)+1])
DNA = DNA.replace ('\n','')

CodonDict= {
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

#print (len(DNA))
protein = ""
#for i in range(0,len(DNA),3):
#	if (DNA[i:i+3] in CodonDict):
#		protein = protein +  CodonDict[DNA[i:i+3]]
#for i in range(1,len(DNA)-2,3):
 #       if (DNA[i:i+3] in CodonDict):
  #              protein = protein +  CodonDict[DNA[i:i+3]]
for i in range(2,len(DNA)-1 ,3):
        if (DNA[i:i+3] in CodonDict):
                protein = protein +  CodonDict[DNA[i:i+3]]


#print (len(protein))
#print (protein)
a=0
b=0 
for i in range(len(protein)):
	a = a + 1
	if (protein [i] == '*'):
		if (a>100):
			b = b + 1
			print (a)
		#	print (i-a)
			print (i)
			print (protein[i-a:i+1])
		a = 0	



print ("Number of >100AA is", b)
