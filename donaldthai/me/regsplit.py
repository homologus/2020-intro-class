
import re

f= open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna", "r")
next(f)
dnaSeq= f.read()
startIndex=0
endIndex=0
genome= re.sub('\n',"",dnaSeq)
frags=0
size=0
lengthns= len(genome)
fragment=""
frags+= len(re.split("GAC[ATGC][ATGC][ATGC][ATGC][ATGC]GTC",genome[0:lengthns-11+0]))-1
print(frags)
