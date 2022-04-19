n, xheight, ywidth = map (int, input().split())

for i in range(n // xheight + 1):
    if (n - i * xheight) % ywidth == 0:
        print(i, (n - i * xheight) // ywidth)
        break
else:
    print(-1)
