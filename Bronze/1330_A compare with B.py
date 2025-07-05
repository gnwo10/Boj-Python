import sys
input = sys.stdin.readline

a, b = map(int,input().split())

if a > b:
    print('>')
if a < b:
    print('<')
if a == b:
    print('==')