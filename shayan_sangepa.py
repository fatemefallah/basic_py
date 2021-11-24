def is_prime(num): #check if it is prime or not
    if num == 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def divs(num): #returns conut of divisors of num
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0 and is_prime(i) == 1:
            cnt += 1
    return cnt

"""
if is_prime(w) == 1:
    for i in range(1, w):
        if is_prime(i) == 1:
            print(i)
elif is_prime(w) == 0:
    for i in range(1, w):
        if
"""
n = int(input())
weights = []
for i in range (0, n + 1):
    w = int(input())
    weights.insert(i, w)

for i in range (0, len(weights) + 1):
    
#print(n)
print(weights)
#print(divs(n))