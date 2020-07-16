f= open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna", "r")
next(f)
dnaSeq= f.read()
genome=""
startIndex=0
endIndex=0
length= len(dnaSeq)
for x in range(length):
        if(dnaSeq[x]!="\n"):
                genome+=dnaSeq[x]
frags=0
size=0
lengthns= len(genome)
fragment=""
for t in range(11):
	for l in range(t,lengthns-11+t,11):
		part= genome[l:l+11]
		size+=11
		if(part[0:3]=="GAC" and part[8:11]=="GTC"):
			endIndex=l
			size-=11
			frags+=1
			startIndex=l+11
			size=0
print(frags)
