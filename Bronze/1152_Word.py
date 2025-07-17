import sys

input = sys.stdin.readline

word = list(input().split())

count = 0

for i in word:

    if i != "":
        count = count + 1

print(count)