x = int(input())
x_digit_cnt= [0 for i in range(10)]
tmp = x
while tmp:
    x_digit_cnt[tmp % 10] += 1
    tmp //= 10
for y in range(x + 1, 1000000):
    y_digit_cnt = [0 for i in range(10)]
    tmp = y
    while tmp:
        y_digit_cnt[tmp % 10] += 1
        tmp //= 10
    for i in range(10):
        if y_digit_cnt[i] != x_digit_cnt[i]:
            break
    else:
        print(y)
        break
else:
    print(0)