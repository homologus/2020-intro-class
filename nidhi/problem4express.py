f = open('/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna', 'r')
s = f.readlines()
finalstr = ''
for p in range(1, len(s)):
        finalstr = finalstr + s[p].rstrip("\n")
a = []
#finalstr = "ATGTCTTGACGGGGGGTCAGACTTT"
#print (len(finalstr))
for i in range(0, len(finalstr)-1):
        if finalstr[i:(i+3)] == "GAC" and finalstr[(i+8):(i+11)] == "GTC":
                print("cuts after" + str(i+4))
                a.append(i+4)
                print("the length is" + str((a[len(a)-1]-a[len(a)-2])))

t = len(a)
#print (t)

for i in range(0,11):
        x = finalstr[(len(finalstr)-i):len(finalstr)]
        y = finalstr[0:(11-i)]
        for z in range(0, 11):
                if xy[z:(z+3)] == "GAC" and xy[(z+8):(z+11)] == "GTC":
                        t = t+1

for i in range(1, len(a)-1):
        if a[i-1]>a[i]:
                c = finalstr[a[len(a)-1]:len(finalstr)-1]
                d = finalstr[0:finalstr[a[0]]]
                print ("length is" + len(cd))
print (t)
