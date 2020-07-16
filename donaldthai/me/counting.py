f= open("SARS-2020.fasta", "r")
next(f)
total=0
genome= f.read()
d= {"A": 0, "T":0, "G":0, "C":0}
length=len(genome)
for i in range(length):
	if(genome[i]!= "\n"):
		d[genome[i]] = d[genome[i]]+1
		total += 1
print(d)
gccontent= (d["G"]+d["C"])/(total)
print("GC-Content: ", gccontent)

