import sys

input = sys.stdin.readline

word = input().strip()

check = list(word)

for i in range(97,123):
    found = False
    count = 0

    for j in check:

        if j == chr(i):
            print(count,end=' ')
            found = True
            break
        count = count + 1
    
    if not found:
        print(-1, end=' ')


    



    

