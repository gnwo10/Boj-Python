import sys

input = sys.stdin.readline

T = int(input())

results = []

for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = ""

    for ch in S:
        result += ch * R
    results.append(result)


for a in results:
    print(a)