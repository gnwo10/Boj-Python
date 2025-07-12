import sys
input = sys.stdin.readline

N = int(input())

b = list(map(int,input().strip()))
sum = 0

for i in range(0,N):
    sum = sum + b[i]

print(sum)
