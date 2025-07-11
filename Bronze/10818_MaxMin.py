import sys

input = sys.stdin.readline

N = int(input())

max_value = -int(1e9)
min_value = int(1e9)

num = list(map(int,input().split()))

for _ in range(N):

    for a in num:

        if a > max_value:
            max_value = a

        if a < min_value:
            min_value = a


print(min_value, max_value)



