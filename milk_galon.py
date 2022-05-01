a, b, c = map(int, input().split())
avg = (a + b + c) / 3.0
if a == b == c:
    print(0)

elif (a == avg or b == avg or c == avg):
    print(1)

else:
    print(2)