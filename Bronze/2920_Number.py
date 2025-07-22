import sys

input = sys.stdin.readline

number = list(map(int,input().split()))

as_ascending = True
ds_descending = True

for i in range(7):

    if number[i] < number[i+1]:
        ds_descending = False

    elif number[i] > number[i+1]:
        as_ascending = False

if as_ascending:
    print("ascending")

elif ds_descending:
    print("descending")

else:
    print("mixed")

    
