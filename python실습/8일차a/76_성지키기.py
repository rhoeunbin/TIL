n, m = map(int,input().split())

for x in range(n):
    for y in range(m):
        



N, M = map(int, input().split())

matrixR = [list(input()) for _ in range(N)]
matrixC = list(map(list, zip(*matrixR)))

result1 = result2 = 0
for i in range(N):
    if 'X' not in matrixR[i]:
        result1 += 1

for j in range(M):
    if 'X' not in matrixC[j]:
        result2 += 1

print(max(result1, result2))


n, m = map(int, input().split())
matrix = []

x = 0
y = 0
for i in range(n):
    a = list(input())
    matrix.append(a)

# in_matrix = list(map(list, zip(*matrix)))

in_matrix = [[0 for n in range(n)] for m in range(m)]

for p in range(n):
    for q in range(m):
        in_matrix[q][p] = matrix[p][q]

for j in matrix:
    if 'X' not in j:
        x +=1
for k in in_matrix:
    if 'X' not in k:
        y +=1
print(max(x,y))