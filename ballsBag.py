n = int(input())
counter = [0 for x in range(210)]
res = list()

for i in range(n):
    opt, col = map(str, input().split())
    col = int(col)
    if opt == '+':
        counter[col] += 1
    else:
        res.append(counter[col])
print(*res, sep="\n")
