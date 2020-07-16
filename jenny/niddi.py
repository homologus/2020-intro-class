fileVar = open('/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna','r')
variable = fileVar.readlines ()
finalstr = ''.join (variable[1:len(variable)+1])
finalstr = finalstr.replace ('\n','')

#finalstr = "AAGAC*****GTCTTA11111GAC12345GTCAAAAAAAAGACxxxxxGTCTTA11111GACzzzzz"
a=[]
for i in range (0, len(finalstr)-1):
	if (finalstr[i:(i+3)] == "GAC" and finalstr[(i+8):(i+11)]=="GTC"):
		a.append(i+4)
t = len(a)
print (t)		

for i in range (0,11):
	x = finalstr[(len(finalstr)-i):len(finalstr)]
	y = finalstr[0:(11-i)]
	j = x + y
	for z in range (0,11):
		if j[z:(z+3)] == "GAC" and j[(z+8):(z+11)] =="GTC" :
			t=t+1
print (t)
