N, M = map(int, input().split())

matrix_A = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_A.append(row)

matrix_B = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_B.append(row)

result_matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(matrix_A[i][j] + matrix_B[i][j])
    result_matrix.append(row)

for row in result_matrix:
    print(" ".join(map(str, row)))
