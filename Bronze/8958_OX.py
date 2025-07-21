import sys
input = sys.stdin.readline

a = int(input())
result = []

for _ in range(a):
    test = input().strip()
    
    count = 0
    max_value = 0

    for ch in test:
        if ch == 'O':
            count += 1
            max_value += count
        else:
            count = 0

    result.append(max_value)

for score in result:
    print(score)
