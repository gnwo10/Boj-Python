import sys

input = sys.stdin.readline

N = int(input())
a = map(int,input().split())

count = 0

def find_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for ch in a:
    if find_prime(ch):
        count += 1


print(count)

