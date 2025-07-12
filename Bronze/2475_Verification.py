import sys
input = sys.stdin.readline

a = map(int,input().split())
sum = 0
value = 0

for num in a:
    sum = sum + num * num

    value = sum % 10


print(value)
