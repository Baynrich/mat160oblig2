import numpy as np
import matplotlib.pyplot as plt
from funcs import jacobi
from funcs import gauss_seidel


def generate_matrix(alpha, N=1000):
    A = []
    for i in range(N):
        a_row = []
        for j in range(N):
            if i == j:
                a_row.append(2 + alpha)
            elif abs(i-j) == 1:
                a_row.append(-1)
            else:
                a_row.append(0)
        A.append(a_row)
    A = np.array(A)
    x_0 = np.array([0] * N)
    b = np.array([1] * N)
    return A, x_0, b

print("Funksjonene vil konvergere for alpha != [-4, 0], fordi begge metodene krever at input-matrisen er strictly diagonally dominant")


alphas = [0.1, 0.2, 0.5, 2]
color_code_gauss_seidel = {
    0.1: "#ccccff",
    0.2: "#6666ff",
    0.5: "#0000ff",
    2: "#000099"
}
color_code_jacobi = {
    0.1: "#ffd9b3",
    0.2: "#ffa64d",
    0.5: "#ff8000",
    2: "#cc6600"
    
}
plt.subplot(211)
for alpha in alphas:
    A, x_0, b = generate_matrix(alpha)
    x, errs = jacobi.solve(A, x_0, b, 20)
    plt.plot(errs, color_code_jacobi[alpha], label=alpha)
plt.title("Jacobi")
plt.yscale("log", base=2.78)
plt.legend()

plt.subplot(212)
for alpha in alphas:
    A, x_0, b = generate_matrix(alpha)
    x, errs = gauss_seidel.solve(A, x_0, b, 20)
    plt.plot(errs, color_code_gauss_seidel[alpha], label=alpha)
plt.title("Gauss-Seidel")
plt.yscale("log", base=2.78)
plt.legend()

plt.show()










