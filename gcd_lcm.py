def gcd(a, b):
    if a > b:
        tmp = a
        a = b
        b = tmp
    while a > 0:
        b = b % a
        tmp = a
        a = b
        b = tmp
    return b
    
def lcm(a, b):
    return a * b // gcd(a, b)
    
n = int(input())
ans = 1
for i in range(1, n):
    if gcd(i, n) == 1:
        ans = lcm(ans, i)
print(ans)