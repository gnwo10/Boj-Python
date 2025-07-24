import sys


input = sys.stdin.readline
t = int(input())

results = []

for i in range(t): # 층수, 호수를 구해야함
    # H : 호텔 층 W: 각방 개수 N : 몇번째 손님
    h, w, n = map(int, input().split())

    # ex) 6 12 10
    # 101 201 301 401 501 601
    # 102 202 302 402 502 602

    floor = n % h
    room = n // h + 1

    if floor == 0:
        floor = h
        room = n // h

    results.append(floor * 100 + room)


for result in results:
    print(result)
