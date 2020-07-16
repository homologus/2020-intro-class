


with open ('small-genome') as fileVar:
	variable = fileVar.readlines ()

tempDNA = variable[1]+variable[2]+variable[3]
#for i in range)
#	if 

#tempDNA="".join(variable[1:len(variable)])
print(tempDNA)
anum=0
tnum=0
gnum=0
cnum=0
for i in range(len(tempDNA)):
	if (tempDNA[i]=="A"):
		anum=anum+1
	if (tempDNA[i]=="T"):
		tnum=tnum+1
	if (tempDNA[i]=="G"):
		gnum=gnum+1
	if (tempDNA[i]=="C"):
		cnum=cnum+1
 
print("There is",anum,"counts of A")
print("There is",tnum,"counts of T")
print("There is",gnum,"counts of G")
print("There is",cnum,"counts of C")

