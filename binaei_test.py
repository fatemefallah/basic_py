n = int(input())
str_in = input()
str_out = input()
con1 = list(str_in)
con2 = list(str_out)
cnt = 0
for i in range(n):
    if str_in[i] != str_out[i]:
        cnt += 1
print(cnt)