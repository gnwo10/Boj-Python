import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()

ab = a + b

print(int(a) + int(b) - int(c))
print(str(ab) - str(c))