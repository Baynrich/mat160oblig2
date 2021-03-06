import numpy as np


def solve(A, x, b, max_iters):
    """
    2b)
    Takes matrix, starting x vector, solution vector and a maximum number of iterations.
    Returns iteratively calculated weights vector and array of each iteration's error.
    """
    assert len(A) == len(A[0]), "A must be N x N"
    for i in range(len(A)):
        pos_row = [abs(ele) for ele in A[i]]
        assert pos_row[i] > sum(pos_row)-pos_row[i], "Input matrix is not strictly diagonally dominant"

    # Split matrix into upper and lower
    L = np.tril(A)
    H = np.triu(A, k=1)

    # Iterate towards true value
    L_inv = np.linalg.inv(L)
    errs = []
    for i in range(max_iters):
        Ux = np.dot(H, x)
        x = np.dot(L_inv, b - Ux)
        errs.append(np.linalg.norm(np.subtract(np.dot(A, x), b)))
    return x, errs