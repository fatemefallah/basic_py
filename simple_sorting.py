n = int(input())
num = list(map(int, input().split()))

for i in range(n):
    for j in range(n - 1):
        if num[i] > num[j]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp
print(*num)
