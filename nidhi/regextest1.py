import re
f = open('/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna', 'r')
s = f.readlines()
finalstr = ''
x = []
for p in range(1, len(s)):
        finalstr = finalstr + s[p].rstrip("\n")

#finalstr = "ATGTCTTGACGGGGGGTCAGACTTT"
oddstr = finalstr + finalstr[0:11]
x = re.search('GAC.....GTC', oddstr)
iter = re.finditer('GAC.....GTC', oddstr)
indices = [x.start(0) for x in iter]
print (indices)
print (len(indices))
for i in range(0, len(indices)-1):
	if len(indices) == 2:
		print ("the length is " + str(len(finalstr)))
	else:
		print ("the length is " + str(indices[i+1]-indices[i]))





#imbecilicstr = finalstr[len(finalstr)-11:len(finalstr)]+finalstr[0:11]
#print (imbecilicstr)
#S = re.search('GAC.....GTC', imbecilicstr)
#if S:
#	print(S)
#	print(len(indices)+1)
	#print(str(len(finalstr[indices[len(indices)-1]]:
#else:
#	print("no")
