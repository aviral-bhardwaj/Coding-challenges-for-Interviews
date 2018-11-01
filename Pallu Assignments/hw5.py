import copy

res=[]

def input_size():
    while True:

        try:
            size = int(input('Enter NXN Board Size \n'))
            if 0 < size < 4:
                print("Enter attlist size of 4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")


def board_size(size):
    board = [0] * size
    for i in range(size):
        board[i] = [0] * size
    return board


def print_solution(solutions, size):
	for sol in solutions:
		t_sol=[]
		for row in sol:
			for i in range(len(row)):
				if row[i]==1:
					t_sol.append(i)
			#print(row)
		res.append(t_sol)
		#print()


def is_safe(board, row, col, size):

    # check row on left side
    for iy in range(col):
        if board[row][iy] == 1:
            return False

    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
            return False
        ix -= 1
        iy -= 1

    jx, jy = row, col
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True


def solve(board, col, size,solutions):
    # base case
    if col >= size:
        return

    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            if col == size - 1:
                add_solution(board,solutions)
                board[i][col] = 0
                return
            solve(board, col + 1, size,solutions)
            board[i][col] = 0


def add_solution(board,solutions):
    """Saves the board state to the global variable 'solutions'"""
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)

def B_Queens(n):
	if n<4:
		return [[]]
	else:
		solutions=[]
		board = board_size(n)
		solve(board,0,n,solutions)
		print_solution(solutions, n)
		return res

print(B_Queens(int(input())))		
		
# size = input_size()
# board = board_size(size)
# solutions = []
# solve(board, 0, size)
# print_solution(solutions, size)
