n = int(input())
num = 0
for i in range(1, n//2):
    num = 2 ** i
    if num > n:
        final = num
        break
print(final)

"""
n = int(input())
ans = 1
while ans<=n:
    ans*=2
print(ans)
"""