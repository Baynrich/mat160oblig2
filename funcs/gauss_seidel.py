import numpy as np


def solve(A, x, b, max_iters):
    assert len(A) == len(A[0]), "A must be N x N"
    for i in range(len(A)):
        pos_row = [abs(ele) for ele in A[i]]
        assert pos_row[i] > sum(pos_row)-pos_row[i], "Input matrix is not strictly diagonally dominant"

    # Split matrix into upper and lower
    L, H = [], []
    for i in range(len(A)):
        l_row, h_row = [], []
        for j in range(len(A[0])):
            if(j <= i):
                l_row.append(A[i][j])
                h_row.append(0)
            else:
                l_row.append(0)
                h_row.append(A[i][j])
        L.append(l_row)
        H.append(h_row)
    # Iterate towards true value
    L_inv = np.linalg.inv(L)
    errs = []
    for i in range(max_iters):
        Ux = np.dot(H, x)
        x = np.dot(L_inv, b - Ux)
        errs.append(np.linalg.norm(np.subtract(np.dot(A, x), b)))
    return x, errs