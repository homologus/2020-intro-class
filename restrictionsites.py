import re
f = open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna")
lines = f.readlines()
genome = ""
for i in range(1, len(lines)):
        for j in range(len(lines[i]) - 1):
                genome = genome + lines[i][j]
s = re.split('GAC[A-Z][A-Z][A-Z][A-Z][A-Z]GTC', genome)
for i in range(len(s)):
        print("Length of sequence " + str(i + 1) + ": " + str(len(s[i])))
print("Total number of fragments: " + str(len(s)))
