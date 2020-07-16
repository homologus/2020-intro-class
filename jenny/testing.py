import re

seq="ATTCGATCT"

# counting A
s= re.sub('A', '', seq)
diff=len(seq)-len(s)
print("count of A =", diff)
