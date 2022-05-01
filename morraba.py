n_jar, k_cap = map(int, input().split())
jams = [int(x) for x in input().split()]
cnt = 0
sum = 0
for i in range(n_jar):
    sum += jams[i]
    jams[i] = 0
for i in range(n_jar+1):
    if sum <= k_cap:
        jams[i] += sum
        cnt += 1
        break
            
    else:
        jams[i] += k_cap
        sum -= k_cap
        cnt += 1
print(n_jar - cnt)

"""
n, k = map(int, input().split())

a = list(map(int, input().split()))

print(((len(a) * k) - sum(a)) // k)

"""