
#fileVar = open('/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna','r')
#variable = fileVar.readlines ()
#DNA = ''.join (variable[1:len(variable)+1])
#DNA = DNA.replace ('\n','')

DNA = "AAGAC*****GTCTTA11111GAC12345GTCAAAAAAAAGACxxxxxGTCTTA11111GACzzzzz"
fragments = []
a=0



for i in range(len(DNA)):
	a=a+1
	if (DNA[i:i+3]=='GAC'and DNA[i+8:i+11]=='GTC'):
		fragments.append(DNA[i-a+1:i+6])
		a=-5
fragments.append(DNA[len(DNA)-a:len(DNA)+1])

print ("The amount of fragemnts is",len(fragments)-1)

print ("The length of the number",1,"fragment is",(len(fragments[0]+fragments[len(fragments)-1])))
for i in range (1,len(fragments)-1):
	print ("The length of the number",i+1,"fragemnt is",(len(fragments[i])))

end = (fragments[len(fragments)-1])
end = (end[::-1])
fragments[0] = end + fragments[0] 


print (fragments[0:3]) 
#for i in range(len(fragments)-1)
#	print (fragments[i])
