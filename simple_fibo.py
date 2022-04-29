n = int(input())
fib_arr = []
fib_arr.insert(1, 1)
fib_arr.insert(2, 1)
i = 1
while i < n:
    fib_arr.insert(i, fib_arr[i - 1] + fib_arr[i - 2])
    i += 1

for i in range(1, n + 1):
    if i in fib_arr:
        print('+', end='')
    else:
        print('-', end='')
"""
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)
def is_fib(n):
    i=1
    while(fib(i)<n):
        i += 1
    if fib(i) == n:
        return 1
    else:
        return 0
    #Instead of this if and else block we could write:
    #return fib(i) == n
    #it returns True if fib(i) == n and 0 otherwise
def print_answer(n):
    if n==0:
        return
    print_answer(n-1)
    if is_fib(n):
        print('+',end='')
    else:
        print('-',end='')
n = int(input())
print_answer(n)
"""