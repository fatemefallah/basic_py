def is_prime(num): #check if it is prime or not
    if num == 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

"""def divs(num): #returns conut of prime divisors of a num
    cnt = 0
    if num == 1:
        cnt = 0
    for i in range(2, num):
        if num % i == 0 and is_prime(i) == 1:
            cnt += 1
    return cnt
"""
def price(weights):
    cnt = 0
    total = 0
    #price
    for i in range(0, len(weights)):
        if weights[i] == 1:
            cnt += 0
        elif is_prime(weights[i]) == 1:
            for j in range(2, weights[i]):
                if is_prime(j) == 1:
                    cnt += 1
        else:
            for k in range(2, weights[i]):
                if weights[i] % k == 0 and is_prime(k) == 1:
                    cnt += 1
    total = cnt
    #with discount
    dis = 0
    if total == 1:
        dis = 0
    elif is_prime(total) == 1:
        for k in range(2, total):
            if is_prime(k) == 1:
                dis += 1
        total = total - dis
    else:
        for y in range(2, total):
            if total % y == 0 and is_prime(y) == 1:
                dis += 1
        total = total - dis
    return total

n = int(input())
weights = []
for i in range (0, n):
    w = int(input())
    weights.insert(i, w)
print(price(weights))