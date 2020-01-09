
def main():
	# Matrix inversion only works for square matrices (nxn)
	n = int(input("Enter matrix n: "))
	matrix = input("Enter matrix elements (rows separated by spaces and columns by commas): ").split(',')
	# Convert matrix entries into list of list with integer elements
	for el in range(n):
		matrix[el] = [int(a) for a in matrix[el].split()]

	for i in range(0, n-1):
		# Check if first pivot is zero
		if matrix[i][i]:
			for k in range(i+1, n):
				# First row multiplier to be subtracted from the second row
				r = matrix[k][i] / matrix[i][i]
				# New row after subtraction
				matrix[k] = [row_k - r * row_i for row_k, row_i in zip(matrix[k], matrix[i])]
		else:
			# Changing zero pivots
			for j in range(i+1, n):
				if matrix[j][i]:
					continue
				else:
					# Swap row i with row j
					temp = matrix[i]
					matrix[i] = matrix[j]
					matrix[j] = temp
					break
			print("Matrix is singular")
			return 0

	print("Matrix is invertible with back-substitution results: ")
	[print(row) for row in matrix]


if __name__ == '__main__':
	main()