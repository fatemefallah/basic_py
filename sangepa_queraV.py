def is_prime(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
        if i*i>=n:
            break
    return 1
def prime_factors(n):
    cnt = 0
    for i in range(1,n+1):
        if (n % i == 0) and is_prime(i):
           cnt += 1
    return cnt
def lesser_primes(n):
    cnt = 0
    for i in range(1,n):
        if is_prime(i):
            cnt += 1
    return cnt
def price(n):
    if is_prime(n):
        return lesser_primes(n)
    else:
        return prime_factors(n)
n = int(input())
cost_sum = 0
for i in range(n):
    c = int(input())
    cost_sum += price(c)
cost_sum -= price(cost_sum)
print(cost_sum)
