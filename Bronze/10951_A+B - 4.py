import sys
input = sys.stdin.readline

a = []
b = []
c = []

while True:
    line = input()
    if not line.strip():
        break

    try:
        x, y = map(int, line.split())
        a.append(x)
        b.append(y)
        c.append(x+y)

    except ValueError:
        break

for i in c:
    print(i)
    



