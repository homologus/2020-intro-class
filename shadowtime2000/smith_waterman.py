import sys
import numpy as np

sequence1 = sys.argv[1]
sequence2 = sys.argv[2]

match = int(sys.argv[3])
mismatch = int(sys.argv[4])
gap = int(sys.argv[5])

matrix = []

first_row = []

first_row.append(0)

for i in sequence2:
	first_row.append(0)

matrix.append(first_row)

row_value_start = []
row_value_start.append(0)

for i in sequence2:
	row_value_start.append(None)

for i in sequence1:
	matrix.append(row_value_start)

letter_row = {"0": "-"}
letter_column = {"0": "-"}

for i in range(1, len(matrix) + 1):
	try:
		letter_row[str(i)] = sequence1[i - 1]
		for j in range(1, len(matrix[i])):
			try:
				letter_column[str(j)] = sequence2[j - 1]
			except IndexError:
				break
	except IndexError:
		break
for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if not matrix[i][j] == 0:
			match_t = letter_row[str(i)] == letter_column[str(j)]
			if (match):
				match_t = match
			else:
				match_t = mismatch
			possibilities = [matrix[i-1][j-1] + match_t, matrix[i-1][j] + gap, matrix[i][j-1] + gap, 0]
			matrix[i][j] = possibilities[np.argmax(possibilites)]
print(matrix)
