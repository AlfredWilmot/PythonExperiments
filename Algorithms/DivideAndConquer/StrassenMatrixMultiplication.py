# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:30:37 2021

@author: Alfred


Strassen's Subcubic Matrix Multiplication Algorithm'

X * Y = Z

--> z_ij = (i_th row of X) * (j_th row of Y) = sum(k=1,n)[x_ik*y_kj]

Best-case matrix multiplication of 2x2 matrices is cubic time O(n^3)

"""


def brute_force_matrix_multiplication(A,B):
    """
    By directly using the definition of matrix multiplication, the best-case running time is cubic O(n^3)
    due to three nested for-loops with indices i,j,k. Note in this implementation the 3rd loop exists as 
    a list comprehension.
    """

    # assume the matrices are square nxn matrices
    n = len(A)
    C = []
    row_i = []
    
    for i in range(n):
        for j in range(n): 
            row_i.append(sum(A[i][k]*B[k][j] for k in range(n)))
            
        C.append(row_i.copy())
        row_i.clear()
    
    return C
                    
