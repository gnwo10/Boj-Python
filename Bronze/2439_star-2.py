import sys
input = sys.stdin.readline

N = int(input())
count = 1

for i in range(N):

    print(" " * (N-1) + "*" * count)
    N = N - 1
    count = count + 1

