fileVar = open('/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna','r')

variable = fileVar.readlines ()
DNA = ''.join (variable[1:len(variable)+1])
DNA = DNA.replace ('\n','')
import re

s=re.findall('GAC[A-Z]{5}GTC',DNA) 
print ("There are" ,len(s), "fragments in DNA")
