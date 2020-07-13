counts = {
	"A": 0,
	"T": 0,
	"C": 0,
	"G": 0
}

file = input("Please give the location of the genome file: ")

genome = ""

with open(file, "r") as f:
	for line in f.readlines():
		if not line[0] == ">":
			genome = genome + line.rstrip()
for i in genome:
	counts[i] = counts[i] + 1

print("GC Content: ", (counts["G"]+counts["C"])/(counts["A"]+counts["T"]+counts["G"]+counts["C"]))
