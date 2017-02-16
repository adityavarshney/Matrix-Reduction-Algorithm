# Aditya Varshney, 2/16/17

# Takes user input. Used to get matrix data.
def take_input():
	rows = int(input("How many rows in the matrix/table? \n"))
	table = []
	for i in range(rows):
		print("Enter row " + str(i + 1) + " values: \n")
		val = input()
		table.append([int(x) for x in val.split()])
	if not all([len(row) == len(table[0]) for row in table]):
		print("Invalid row length.")
		return take_input();
	return table

# Reduces a matrix by processing rows and columns recursively
# matrix: the matrix to be reduce
# index: the column/row containing the main diagonal value
def reduce(matrix, index = 0):
	if index == len(matrix):
		return matrix
	diagonal_value = matrix[index][index]
	if int(diagonal_value) != 0:
		for column in range(len(matrix[index])):
			matrix[index][column] /= diagonal_value # gets (index,index) to 1 and manipulates rest of row
		this_row = matrix[index]
		for row in range(len(matrix)):
			if row != index:	
				mult_factor = matrix[row][index]
				for column in range(len(matrix[row])):
					matrix[row][column] -= mult_factor * this_row[column]
	return reduce(matrix, index + 1)


matrix = print(reduce(take_input()))


#
# Test methods used to check reduce operations.
#
def test():
	passed = test_case(reduce([[1, 5], [2,4]]), [[1.0, 0.0], [0.0, 1.0]])
	passed = test_case(reduce([[2, 4],[1, 5]]), [[1.0, 0.0], [0.0, 1.0]])
	passed = test_case(reduce([[50, 10],[60, 0]]), [[1.0, 0.0], [0.0, 1.0]])
	passed = test_case(reduce([[1, 2, 3],[1, 2, 3]]), [[1.0, 2.0, 3.0], [0.0, 0.0, 0.0]])
	passed = test_case(reduce([[1, 2, 3],[1, 2, 3],[4, 8, 12]]), [[1.0, 2.0, 3.0], [0.0, 0.0, 0.0],[0.0, 0.0, 0.0]])
	passed = test_case(reduce([[0,0,0],[0,0,0],[0,0,0]]), [[0,0,0],[0,0,0],[0,0,0]])
	print(passed)

def test_case(actual, expected):
	print(actual)
	return actual == expected