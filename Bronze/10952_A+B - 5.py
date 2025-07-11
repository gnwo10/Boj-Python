import sys
input = sys.stdin.readline


a = []
b = []
c = []

while True:

    line = input()

    if not line.strip():
        continue

    try:
        x, y = map(int,line.split())
        if x == 0 and y == 0:
            break
    
        a.append(x)
        b.append(y)
        c.append(x+y)


    except ValueError:
        break

for i in c:
    print(i)

    



