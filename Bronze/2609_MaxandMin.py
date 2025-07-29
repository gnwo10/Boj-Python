import sys

input = sys.stdin.readline

a, b = map(int,input().split())

d = max(a,b)

result = 1
for i in range(1, min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        result = i

print(result)

arr = 1
while True:
    result2 = d * arr

    if result2 % a == 0 and result2 % b == 0:
        print(result2)
        break
    arr = arr + 1

