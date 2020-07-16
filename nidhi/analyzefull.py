f = open('/share/SARS/SARS-2020.fasta')
s = f.readlines()
finalstr = ''
for p in range(1, len(s)):
	finalstr = finalstr + s[p].rstrip("\n")
m = finalstr
for j in range(0, len(m)-3):
	l = [m[j], m[j+1], m[j+2], m[j+3]]
	k = [m[j], m[j+1], m[j+2], m[j+3]]
	for i in range(0, 4):
		if (l[i] == 'A'):
				l[i] = 'T'
		elif (l[i] == 'T'):
				l[i] = 'A'
		elif (l[i] == 'G'):
				l[i] = 'C'
		elif (l[i] == 'C'):
				l[i] = 'G'
	l.reverse ()
	listToStr = ''.join(l)
	listToStrog = ''.join(k)
	if (listToStr == listToStrog):
		print(j)
