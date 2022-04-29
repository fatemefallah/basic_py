n, str = input().split()
n = int(n)
res = []
for i in range(n):
    res.append('copy of')
res.append(str)
print(*res)