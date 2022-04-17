s = input()
p = input()

for i in range(len(s) - 1):
    flag = True
    for j in range(len(p) - 1):
        if (0 <= i + j < len(s)):
            if s[i + j] != p[j]:
                flag = False
        else:
            flag = False
    if flag == True:
        print(i + 1, end=" ")
        
        s = input()
p = input()