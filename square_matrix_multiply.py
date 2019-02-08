import numpy as np
# Stassen's Algorithm for matrix multiplication
def square_matrix_multiply(A,B):
    n = len(A)
    c = np.zeros((2,2))
    for i in range(0,n):
        for j in range(0, n):
            c[i][j] = 0
            for k in range(0,n):
                c[i][j] = c[i][j] + A[i][k]*B[k][j]
    return c


# Main Program
A = [[2, 2],
     [2, 2]]

B = [[4, 3],
     [2, 1]]

c = square_matrix_multiply(A, B)

print(c)
