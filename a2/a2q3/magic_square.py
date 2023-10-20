'''Magic Square

https://en.wikipedia.org/wiki/Magic_square

A magic square is a n * n square grid filled with distinct positive integers in
the range 1, 2, ..., n^2 such that each cell contains a different integer and
the sum of the integers in each row, column, and diagonal is equal.

'''

#from z3 import Solver, sat, unsat
from z3 import *


def solve_magic_square(n, r, c, val):
    solver = Solver()
    #Array with integer
    arr=[[Int('a_%d_%d'%(i+1,j+1)) for i in range(n)] for j in range(n)]

    #1 ≤ val ≤ n**2
    condition = [And(arr[i][j]>=1,arr[i][j]<=n**2) for i in range(n) for j in range(n)]

    #square grid filled with distinct positive integers
    condition += [Distinct([arr[i][j] for i in range(n) for j in range(n)])]

    #store the sum of the integers in each row, column, and diagonal
    total = 0
    total_row = [0 for i in range(n)]
    total_column = [0 for i in range(n)]
    total_diagonal = [0 for i in range(2)]

    #store the sum of the integers in the first row
    for i in range(n):
        total += arr[0][i]

    #store the sum of the integers in each row, column, diagonal
    for i in range(n):
        for j in range(n):
            total_row[i] += arr[i][j]
    for i in range(n):
        for j in range(n):
            total_column[i] += arr[j][i]
    for i in range(n):
        total_diagonal[0] += arr[i][i]
        total_diagonal[1] += arr[i][n-i-1]

    #Compare the sum in the first row with each row, column, diagonal
    for i in range(n):
        condition += [total == total_row[i]]
        condition += [total == total_column[i]]
    for i in range(2):
        condition += [total == total_diagonal[i]]

    #the value val filled at location (r, c)
    condition = condition+[arr[r][c] == val]

    #add conditions to solver
    solver.add(condition)

    if solver.check() == sat:
        mod = solver.model()
        res = [[mod.evaluate(arr[i][j]).as_long() for j in range(n)]for i in range(n)]

        # CREATE RESULT MAGIC SQUARE BASED ON THE MODEL FROM THE SOLVER

        return res
    else:
        return None


def print_square(square):
    '''
    Prints a magic square as a square on the console
    '''
    n = len(square)

    assert n > 0
    for i in range(n):
        assert len(square[i]) == n

    for i in range(n):
        line = []
        for j in range(n):
            line.append(str(square[i][j]))
        print('\t'.join(line))


def puzzle(n, r, c, val):
    res = solve_magic_square(n, r, c, val)
    if res is None:
        print('No solution!')
    else:
        print('Solution:')
        print_square(res)


if __name__ == '__main__':
    n = 3
    r = 1
    c = 1
    val = 5
    puzzle(n, r, c, val)
