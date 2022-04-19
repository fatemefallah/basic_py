n, m = map(int, input().split())
#t = [[input()] for i in range(n)] this brings 3D lists and thats WRONG
t = [input() for i in range(n)]
#matrix= [[input() for j in range(m)] for i in range(n)]
s = input()
size = len(s)
ans = 0
#horizontal
for i in range(n):
    for j in range (m - size + 1):
        diff = 0
        for k in range(size):
            if s[k] != t[i][k + j]:
                diff = 1
        if diff == 0:
            ans += 1

#vertical
for i in range(n - size + 1):
    for j in range (m):
        diff = 0
        for k in range(size):
            if s[k] != t[i + k][j]:
                diff = 1
        if diff == 0:
            ans += 1
print(ans)