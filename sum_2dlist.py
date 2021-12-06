n, m = map(int, input().split())
a = [[0] * m for i in range(n)]
b = [[0] * m for j in range(n)]
c = [[0] * m for k in range(n)]
# the first line of input is the number of rows of the array
a = [[int(l) for l in input().split()] for i in range(n)]
b = [[int(m) for m in input().split()] for i in range(n)]
for p in range (n):
    for j in range(m):
        c[p][j] = a[p][j] + b[p][j]
for e in range(n):
    for x in range(m):
        print(c[e][x], end=" ")
    print()