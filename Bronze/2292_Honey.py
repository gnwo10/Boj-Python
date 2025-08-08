import sys

input = sys.stdin.readline

# 1 1
# 2-7 5 2
# 8-19 11 3
# 20-37 17 4 
# 38-61 23 5

a = int(input())

def get_ring(n):
    i, max_num = 1, 1
    while max_num < n:
        max_num += 6 * i
        i += 1
    return i


print(get_ring(a))

