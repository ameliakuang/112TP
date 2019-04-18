# first randomly generate tiles, 
# and then use backtracking to generate the board
'''
-1: is for player, and a normal tile should be placed in the board
0: normal tiles
1,2,3,4: direction tiles
5: portal tiles
6: jump tiles
7: cube 
8：target tiles
'''

def solve(board):
	


def generateBoard(n):
    board = [ [ None ] * n for row in range(n)]
    board[0][0] = -1
    solution = solve(board)
    if solution != None:
        return solution
    return None