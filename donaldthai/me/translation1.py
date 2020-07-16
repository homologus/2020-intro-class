f= open("small-genome", "r")
next(f)
total=0
dnaSeq= f.read()
proteinSeq=""
length= len(dnaSeq)
d= {
"TTT" : "F-", "TTC" : "F-",
"TTA" : "L-", "TTG" : "L-", "CTT" : "L-", "CTC" : "L-", "CTA" : "L-", "CTG" : "L-",
"ATT" : "I-", "ATC" : "I-", "ATA" : "I-",
"ATG" : "M-",
"GTT" : "V-", "GTC" : "V-", "GTA" : "V-", "GTG" : "V-",
"TCT" : "S-", "TCC" : "S-", "TCA" : "S-", "TCG" : "S-", "AGT" : "S-", "AGC" : "S-",
"CCT" : "P-", "CCC" : "P-", "CCA" : "P-", "CCG" : "P-",
"ACT" : "T-", "ACC" : "T-", "ACA" : "T-", "ACG" : "T-",
"GCT" : "A-", "GCC" : "A-", "GCA" : "A-", "GCG" : "A-",
"TAT" : "Y-", "TAC" : "Y-",
"CAT" : "H-", "CAC" : "H-",
"CAA" : "Q-", "CAG" : "Q-",
"AAT" : "N-", "AAC" : "N-",
"AAA" : "K-", "AAG" : "K-",
"GAT" : "D-", "GAC" : "D-",
"GAA" : "E-", "GAG" : "E-",
"TGT" : "C-", "TGC" : "C-",
"TGG" : "W-",
"CGT" : "R-", "CGC" : "R-", "CGA" : "R-", "CGG" : "R-", "AGA" : "R-", "AGG" : "R-",
"GGT" : "G-", "GGC" : "G-", "GGA" : "G-", "GGG" : "G-",
"TGA" : "*", "TAG" : "*", "TAA" : "*"
}
dnaSeq.replace("\n", "")
print(dnaSeq)

bigprotein=0
