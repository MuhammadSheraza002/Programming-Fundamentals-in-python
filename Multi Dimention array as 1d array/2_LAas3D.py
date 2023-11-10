def showMatrix(m, pags, rows, cols):
	for p in range(pags):
		print("Page # ", p)
		for r in range(rows):
			for c in range(cols):
				i = p*pags*cols + r*cols + c
				print(m[i], end="\t")
			print()
		print()

def main():
	dm = [3, 4, 2, 7, 7, 3, 4, 2, 7, 3, 4, 2, 0, 9, 2, 7, 6, 4, 11, 7, 3, -5, 2, 3]
	print("Values in 1D array are", len(dm), end="\n\n\n")

	print("A 3 X 4 X 2 matrix")
	showMatrix(dm, 3, 4, 2)  # order is 3 X 4 * 2

	print("A 2 X 2 X 6 matrix")
	showMatrix(dm, 2, 2, 6)  # order is 2 X 2 * 2

	print("A 1 X 2 X 12 matrix")
	showMatrix(dm, 1, 2, 12)  # order is 1 X 2 * 6

main()