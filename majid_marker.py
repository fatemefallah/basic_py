n = int(input())
counter = [0 for x in range(101)]
inp = input().split()
max_clr = 0

for i in range(n):
    inp[i] = int(inp[i])
    counter[inp[i]] += 1
    if counter[inp[i]] > max_clr:
        max_clr = inp[i]

answer = -1
for j in range(1, max_clr + 1):
    if counter[j] > 0:
        if answer == -1 or counter[answer] > counter[j] or (counter[answer] == counter[j] and j < answer):
            answer = j
print(answer)

"""
maxn = 100
counter = [0 for i in range(maxn)]
n = int(input())

xs = [int(x) for x in input().split()]
for x in xs:
    counter[x - 1] += 1

mn = -1
for i in range(maxn):
    if counter[i] > 0 and (mn == -1 or counter[mn] > counter[i]):
    	mn = i

print(mn + 1)
    

"""