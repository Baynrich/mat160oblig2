import numpy as np


def solve(A, x, b, max_iters):
    assert len(A) == len(A[0]), "Input matrix must be N x N"
    for i in range(len(A)):
        pos_row = [abs(ele) for ele in A[i]]
        assert pos_row[i] > sum(pos_row)-pos_row[i], "Input matrix is not strictly diagonally dominant"
    D = np.diag(np.diag(A))
    LH = np.subtract(A, D)
    errs = []
    D_inv = np.linalg.inv(D)

    for i in range(max_iters):
        LHx = np.dot(LH, x)
        x = np.dot(D_inv, b - LHx)
        errs.append(np.linalg.norm(np.subtract(np.dot(A, x), b)))
    return x, errs
