import sys
input = sys.stdin.readline

H, M = map(int,input().split())
a_value = 0
d_value = 0

if M >= 45:
    a_value = M - 45

elif M < 45:
    d_value = -(M - 45)
    a_value = 60 - d_value
    H -= 1
    if H < 0:
        H = 23


print(H,a_value)

