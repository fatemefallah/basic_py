n, k = map(int, input().split())
num = [int(x) for x in input().split()]
num.sort()
ans = float('inf')

for i in range(n):
    cnt = 1
    p = i + 1
    while p < n:
        if num[p] != num[p - 1]:
            cnt += 1
            if cnt == k:
                ans = min(ans, num[p] - num[i])
        p += 1
        
    if (i == n - 1) and ans == float('inf'):
        ans = -1
    if k == 1:
        ans = 0
print(ans)