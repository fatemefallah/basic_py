N, M = map(int, input().split())
pr = [[0] * N for i in range(N)]
loc = [[0] * 2 for j in range(M)]
total = 0
for i in range(N):
    inp = input().split()
    for j in range(N):
        pr[i][j] = int(inp[j])
        
for k in range(M):
    xy = input().split()
    for p in range(2):
        loc[k][p] = int(xy[p])

for l in range(M):
    total += pr[loc[l][0] - 1][loc[l][1] - 1]
print(total)
