n = int(input())
L1 = [0] * n
L2 = [0] * n
L3 = [0] * n

L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

for k in range(n):
    L3[k] = L1[k] + L2[k]
    
print(*L3)