import sys

input = sys.stdin.readline

# 5C2 5! / (2! * (5-2)!), n! / (k! * (n - k)!)

a, b = map(int,input().split())

fin_result = 0

def pac(c):
    result = 1
    for i in range(1,c+1):
        result = result * i

    return result

fin_result = int((pac(a)) / (pac(b) * pac(a-b)))

print(fin_result)
