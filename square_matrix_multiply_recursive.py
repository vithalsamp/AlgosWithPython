import numpy as np
# Stassen's Algorithm for matrix multiplication


def square_matrix_multiply_recursive(A,B):
    np.matrix(A)
    np.matrix(B)
    print(A, B)
    n = len((A))
    C = np.zeros((2, 2))
    print(C)

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        C[0][0] = square_matrix_multiply_recursive(A[0][0], B[0][0]) + square_matrix_multiply_recursive(A[0][1],
                                                                                                        B[1][0])

        C[0][1] = square_matrix_multiply_recursive(A[0][0], B[0][1]) + square_matrix_multiply_recursive(A[0][1],
                                                                                                        B[1][1])
        C[1][0] = square_matrix_multiply_recursive(A[1][0], B[0][0]) + square_matrix_multiply_recursive(A[1][1],
                                                                                                        B[1][0])
        C[1][1] = square_matrix_multiply_recursive(A[1][0], B[0][1]) + square_matrix_multiply_recursive(A[1][1],
                                                                                                        B[1][1])
    return C


# Main Program
A = [[2, 2],
     [2, 2]]

B = [[4, 3],
     [2, 1]]

#print(len(A))

c = square_matrix_multiply_recursive(A, B)

print(c)