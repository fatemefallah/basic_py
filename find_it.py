
n, q = map(int, input().split())
num = [int(x) for x in input().split()]
arr = [0] * q
for i in range(q):
    inp = input().split()
    arr[i] = int(inp[1])
for j in range(q):
    L = 0
    R = q
    while R - L > 1:
        mid = (L + R) // 2
        if num[mid] <= arr[j]:
            L = mid
        elif num[mid] > arr[j]:
            R = mid

    if num[L] == arr[j]:
        print(1)
    else:
        print(0)
"""
n, q = map(int, input().split())
num = [int(x) for x in input().split()]
arr = [0] * q
for i in range(q):
    inp = input().split()
    arr[i] = int(inp[1])

for j in range(q):
    L = 0
    R = q
    while L < R :
        mid = (L + R) // 2
        if num[mid] == arr[j] :
            L = mid
            R = mid + 1
            break
        elif num[mid] > arr[j] :
            R = mid
        elif num[mid] < arr[j] :
            L = mid + 1
    if num[L] == arr[j] :
        print(1)
    else:
        print(0)
"""