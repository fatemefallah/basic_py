n = int(input())
names = []
for i in range(n):
  names.append(len(set(input())))
print(max(names))
"""
n = int(input())
answer = 0
for i in range(n):
    s = input()
    distinct_characters = len(s)
    
    for j in range(len(s)):
        duplicate = 0
        for k in range(j):
            if s[j] == s[k]:
                duplicate = 1
        distinct_characters -= duplicate
    
    if distinct_characters > answer:
        answer = distinct_characters

print(answer)"""
