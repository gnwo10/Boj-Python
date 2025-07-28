import sys

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
count = [0] * 10001

for _ in range(N):
    num = int(input())
    count[num] = count[num] + 1

for i in range(1,10001):
    for _ in range(count[i]):
        output(f"{i}\n")