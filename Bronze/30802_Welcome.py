import sys
input = sys.stdin.readline

# 티셔츠 한장과 펜 한 자루 포함된 웰컴 키트
# 1kit = 1Tshirt + 1 pen

N = int(input()) # 참가자의 수
# 3 1 4 1 5 9

num = list(map(int,input().strip().split())) # 티셔츠 사이즈별 신청자 수
# S, M, L, XL, XXL, XXXL 
# 1 1 1 1 1 2 사이즈 티셔츠 1묶음씩 구매, XXXL 사이즈 티셔츠 2묶음 구매
# 5 5 5 5 5 10 
# 

# 티셔츠 묶음 5개, 펜의 묶음 7개

T, P = map(int,input().strip().split()) # 정수 티셔츠와 펜의 묶음수
# 5, 7

# 티셔츠를 T장씩 최소 몇 묶음 주문?
# 7
# P자루씩 최대 몇 묶음 주문, 그때 펜을 한자루씩 몇개 주문?
# 3, 2 # 7 * 3 한자루씩 2개 + 2

# 티셔츠 최소 몇 묶음 주문해야하는지 로직
count = 0
for ch in num:
    count = count + (ch + T - 1) // T

print(count)

# 펜을 P자루씩 최대 몇 묶음 개수, 펜을 한자루씩 몇개?

a = N // P
b = N % P

print(a, b)

