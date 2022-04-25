# Given number as int array, this function finds the
# greatest number and returns the number as integer
def findNext(number,n):
	
	# Start from the right most digit and find the first
	# digit that is smaller than the digit next to it
	for i in range(n - 1, 0, -1):
		if number[i] > number[i-1]:
			break

	# If no such digit found,then all numbers are in
	# descending order, no greater number is possible
	if i == 1 and number[i] <= number[i-1]:
		print (0)
		return
		
	# Find the smallest digit on the right side of
	# (i-1)'th digit that is greater than number[i-1]
	x = number[i-1]
	smallest = i
	for j in range(i+1,n):
		if number[j] > x and number[j] < number[smallest]:
			smallest = j
		
	# Swapping the above found smallest digit with (i-1)'th
	number[smallest],number[i-1] = number[i-1], number[smallest]
	
	# X is the final number, in integer datatype
	x = 0
	# Converting list upto i-1 into number
	for j in range(i):
		x = x * 10 + number[j]
	
	# Sort the digits after i-1 in ascending order
	number = sorted(number[i:])
	# converting the remaining sorted digits into number
	for j in range(n-i):
		x = x * 10 + number[j]
	
	print (x)

digits = input()
number = list(map(int ,digits))
findNext(number, len(digits))


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
        
