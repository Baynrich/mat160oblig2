
def solve(U, b):
    assert len(U) == len(U[0]), "U must be NxN matrix"
    assert len(U) == len(b), "Matrix and solution vector do not match"
    """ Takes matrix, solution vector. returns weights vector. """
    x = []
    for i in range(len(U)):
        offset = 0
        j = 0
        while j < i:
            offset += U[len(U)-1 - i][len(U[i])-1 - j] * x[j]
            j += 1
        b_i = b[len(b)-1 - i]
        b_i -= offset
        x_i = b_i / U[len(U)-1 - i][len(U)-1 - i]
        x.append(x_i)
    x.reverse()
    return x
