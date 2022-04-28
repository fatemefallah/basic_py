L, R = map(int, input().split())
max = 100000
res = [1]
n = 1
while n < max:
    for i in range(n):
        if i + n < max:
            res.append(1 - res[i])
    n *= 2

for i in range(L - 1, R):
    print(res[i], end='')
print()

"""firstString = "1"
lastString = "1"
# Give Input
input = input()
tempInput = input.split(" ")
L = int(tempInput[0])
R = int(tempInput[1])
temp = None
i = 0
while (len(firstString) <= R + 1) :
    if (i == 0) :
        firstString = "10"
        lastString = "01"
    temp = lastString + firstString
    firstString += lastString
    lastString = temp
    i += 1
print(firstString[L - 1:R])"""