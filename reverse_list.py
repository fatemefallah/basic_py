l = []
while 1 == 1 :
    n = int(input())
    if n != 0:
        l.append(n)
    elif n == 0:
        break
l.reverse()
"""for i in range(0, len(l)):
    print(l[i], end=' ')"""
print(*l, sep="\n")