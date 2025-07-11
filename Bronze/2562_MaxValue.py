import sys
input = sys.stdin.readline

count = 0
max_val = 0

for i in range(9):
    num = int(input())

    if num > max_val:
        max_val = num
        count = i + 1


print(max_val)
print(count)