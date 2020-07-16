f= open("SARS-2020.fasta", "r")
next(f)
total=0
dnaSeq= f.read()
proteinSeq=""
length= len(dnaSeq)
d= {
"TTT" : "F", "TTC" : "F",
"TTA" : "L", "TTG" : "L", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L",
"ATT" : "I", "ATC" : "I", "ATA" : "I",
"ATG" : "M",
"GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG" : "V",
"TCT" : "S", "TCC" : "S", "TCA" : "S", "TCG" : "S", "AGT" : "S", "AGC" : "S",
"CCT" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P",
"ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T",
"GCT" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A",
"TAT" : "Y", "TAC" : "Y",
"CAT" : "H", "CAC" : "H",
"CAA" : "Q", "CAG" : "Q",
"AAT" : "N", "AAC" : "N",
"AAA" : "K", "AAG" : "K",
"GAT" : "D", "GAC" : "D",
"GAA" : "E", "GAG" : "E",
"TGT" : "C", "TGC" : "C",
"TGG" : "W",
"CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AGA" : "R", "AGG" : "R",
"GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G",
"TGA" : "*", "TAG" : "*", "TAA" : "*"
}
genome=""
startIndex=0
endIndex=0
for x in range(length):
        if(dnaSeq[x]!="\n"):
                genome+=dnaSeq[x]
lengthns= len(genome)
bigprotein=0
swapDna= ""
reverseComp = ""
for x in range(0, lengthns):
    if (genome[x] == "A"):
        swapDna += "T"
    elif (genome[x] == "T"):
        swapDna += "A"
    elif (genome[x] == "G"):
        swapDna += "C"
    elif (genome[x] == "C"):
        swapDna += "G"
for i in range(len(swapDna)-1,-1,-1):
    reverseComp += swapDna[i]
for t in range(3):
        for l in range(t, lengthns-2, 3):
                if ((reverseComp[l:l+3] == "TGA" or reverseComp[l:l+3] == "TAA" or reverseComp[l:l+3] == "TAG") or l+2==lengthns):
                        proteinSeq += (d[reverseComp[l:l+3]])
                        endIndex=l+3
                        if(total>100):
                                print(proteinSeq, "Index: [", startIndex,",", endIndex,"]" , "Length:", total)
                                bigprotein+=1
                        proteinSeq=""
                        total=0
                        startIndex=l+3
                else:
                        proteinSeq += (d[reverseComp[l:l+3]])
                        total+=1
print(bigprotein)

