import sys
input = sys.stdin.readline

T = int(input())
c = [0] * T

for i in range(0,T):
    a,b = list(map(int,input().split()))
    c[i] = a + b

for i in range(0,T):
    print(c[i])
