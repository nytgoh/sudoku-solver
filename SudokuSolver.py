'''
A Sudoku 9x9 solver utilising backtracking. 
It takes in a 9x9 2-dimensional array within the main() function and prints out a solution if one exists.
'''

from itertools import *

def isValid(num, pos, problem):
	''' Checks if a number is unique in its 9x9 box, horizontal line and vertical line '''

	i, j = pos

	# row check
	if (num in problem[i]):
		return False

	# col check
	for row in range(9):
		if (num == problem[row][j]):
			return False

	rowsToCheck = []
	colsToCheck = []
	if (i < 3):
		rowsToCheck = [0, 1, 2]
	elif (i < 6):
		rowsToCheck = [3, 4, 5]
	else:
		rowsToCheck = [6, 7, 8]

	if (j < 3):
		colsToCheck = [0, 1, 2]
	elif (j < 6):
		colsToCheck = [3, 4, 5]
	else:
		colsToCheck = [6, 7, 8]

	# box check
	for r, c in list(product(rowsToCheck, colsToCheck)):
		if (num == problem[r][c]):
			return False

	return True # all tests passed


def backTrack(pos, problem, changedPositions):
	''' Returns to previously assigned answers to locate a different solution to continue. Used to escape deadends.'''
	
	i, j = pos
	newPos = (-1,-1)
	found = False

	for row in range(i, -1, -1):
		for col in reversed(changedPositions[row]):
			found = False
			for num in range(problem[row][col]+1, 10):
				if (isValid(num, (row, col), problem)):
					problem[row][col] = num
					newPos = (row, col)
					found = True
					break

			if (found):
				break
			else:
				changedPositions[row].remove(col)
				problem[row][col] = 0

		if (found):
			break

	return newPos

def solve(problem):
	''' Solves a sudoku puzzle utilising backtracking. Problem is provided as a 2D list.'''

	changedPositions = {
		0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []
		}

	i, j = 0, 0
	while i < 9:
		j = 0
		while j < 9:
			if (not problem[i][j] == 0):
				j += 1
				continue

			foundConflict = False
			for num in range(9):
				if (isValid(num+1, (i, j), problem)):
					problem[i][j] = num+1
					changedPositions[i] += [j]
					foundConflict = True
					break

			if (not foundConflict):
				i, j = backTrack((i, j), problem, changedPositions)


			if i == -1:
				return "No Solution"

			j += 1
		i += 1

	return "Solved"

def main():
	''' Main hub. Inputs are placed here. Solver function called. Output strings are produced.'''

	problem = [
		[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,7,9]
			]

	response = solve(problem)

	# ------------- Print Solution -------------

	if response == "No Solution":
		print("There is no solution to this problem.")
	else:
		print("Solution Found: ")
		print()

		for i in range(9):
			for j in range(9):
				print(problem[i][j], end=" ")

				if j == 2 or j == 5:
					print("| ", end=" ")

			if i == 2 or i == 5:
				print()
				print("-----------------------")
			else:
				print()

		print()


main()