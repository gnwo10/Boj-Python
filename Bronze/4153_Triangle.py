import sys

input = sys.stdin.readline

# a : 변 b : 변 c : 빗변

number = True

result = []

while number == True:
    a, b, c = map(int,input().split())

    if a == 0 and b == 0 and c == 0:
        break

    output = [a, b ,c]
    output.sort()


    if output[2] ** 2 == output[0] ** 2 + output[1] ** 2:
        result.append("right")

    else:
        result.append("wrong")



for ch in result:
    print(ch)
    