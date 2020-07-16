import numpy as np

seq1= "CGTGAATTCAT"
seq2="GACTTAC"
mat= np.array([0,0])
mat.resize(len(seq2)+1,len(seq1)+1)
scores=[0,0,0,0]

#Scoring: Match=5; Gap=-4, Mismatch=-3

def score(a,b):
        if(a==b):
                return 5
        else:
                return -3


for x in range(1,len(seq2)+1):
	for y in range(1,len(seq1)+1):
		scores= [mat[x-1,y-1]+score(seq1[y-1],seq2[x-1]), mat[x,y-1]-4, mat[x-1,y]-4,0]
		big=0
		for t in range(len(scores)):
			if(scores[t]>big):
				big= scores[t]
		mat[x,y]=big
print(mat)

#Backtracking

big=0
xcoor=[]
ycoor=[]
scoreseq1=""
scoreseq2=""
index=0
for x in range(1,len(seq2)+1):
	for y in range(1,len(seq1)+1):
		if(mat[x,y]>big):
			big=mat[x,y]
for x in range(1,len(seq2)+1):
	for y in range(1,len(seq1)+1):
		if(mat[x,y]==big):
			xcoor.append(x)
			ycoor.append(y)
print(xcoor,ycoor)
for x in range(len(xcoor)):
	num1=xcoor[x]
	num2=ycoor[x]
	scoreseq.append(mat[xcoor[x],ycoor[x]])
	while(mat[num1, num2-1]!=0 and mat[num1-1, num2-1]!=0):
		if(mat[num1, num2-1]>mat[num1-1, num2-1] and mat[num1, num2-1]>mat[num1-1, num2]):
			scoreseq.append(mat[num1, num2-1])
			num1=num1
			num2=num2-1
		else:
			scoreseq.append(mat[num1-1, num2-1])
			num1=num1-1
			num2=num2-1
			print(scoreseq)
	index=len(scoreseq)-1
print(scoreseq)

