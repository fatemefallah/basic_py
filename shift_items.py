n, x = map(int, input().split())
l = list(map(int, input().split()))
for i in range(x):
    tmp = l[-1]
    l.insert(0, tmp)
    l.pop(-1)
print(*l)