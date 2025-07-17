import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

multiply = a * b * c
result = list(map(int,str(multiply)))

count = [0] * 10

for i in result:

    if i == 0:
        count[0] = count[0] + 1

    if i == 1:
        count[1] = count[1] + 1

    if i == 2:
        count[2] = count[2] + 1

    if i == 3:
        count[3] = count[3] + 1

    if i == 4:
        count[4] = count[4] + 1

    if i == 5:
        count[5] = count[5] + 1

    if i == 6:
        count[6] = count[6] + 1

    if i == 7:
        count[7] = count[7] + 1

    if i == 8:
        count[8] = count[8] + 1

    if i == 9:
        count[9] = count[9] + 1

for i in range(0,10):
    print(count[i])

