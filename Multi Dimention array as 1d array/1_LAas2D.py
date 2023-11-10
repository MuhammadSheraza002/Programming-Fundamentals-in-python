def showMatrix(m, rows, cols):
	for j in range(rows):
		for k in range(cols):
			i = j*cols+k
			print(m[i], end="\t")
		print()

def main():
	dm2 = [3, 4, 2, 7]
	print("A 2 X 2 matrix")
	showMatrix(dm2, 2, 2)  # order is 2 X 2

	dm3 = [3, 4, 2, 7, 5, -3, 7, 0, 2];
	print("A 3 X 3 matrix")
	showMatrix(dm3, 3, 3);  # order is 3 X 3

	dm4 = [3, 4, 2, 7, 3, 4, 2, 0, 3, 9, 2, 7, 6, 4, 11, 7, 3, -5, 2, 3]
	print("A 4 X 4 matrix")
	showMatrix(dm4, 4, 4);  # order is 4 X 4
	
	print("A 8 X 2 matrix")
	showMatrix(dm4, 8, 2);  # order is 8 X 2
	print("A 8 X 2 matrix")
	showMatrix(dm4, 2, 8);  # order is 2 X 8

	dm7 = [v for v in range(49)]
	print("A 7 X 7 matrix")
	showMatrix(dm7, 7, 7);  # order is 7 X 7

main()