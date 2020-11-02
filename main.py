from funcs import back_substitution

U = []
for i in range(10):
    row = []
    for j in range(10):
        if j < i:
            row.append(0)
        elif j == i:
            row.append(1)
        else:
            row.append(-1)
    U.append(row)
b = [1]*10

print(U)
print(b)
print(back_substitution.solve(U, b))
