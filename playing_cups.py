n, pos = input().split()

for i in range(int(n)):
    inp = input()
    if inp[0] == pos:
        pos = inp[2]

    elif inp[2] == pos:
        pos = inp[0]

print(pos)