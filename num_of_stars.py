n, m = map(int, input().split())
tbl = [[0] * m for i in range(n)]
stars = 0
for i in range(n):
    inp = input()
    for j in range(m):
        tbl[i][j] = inp[j]
        if tbl[i][j] == '*':
            stars += 1
print(stars)