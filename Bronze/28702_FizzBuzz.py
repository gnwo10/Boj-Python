import sys

input = sys.stdin.readline

# 리스트에 저장 후 그 값이랑 비교해서 출력
# 다음값을 구하고 그 값을 변환

text = [input().strip() for _ in range(3)]

def is_number(s):
    try:
        int(s)
        return True
    except:
        return False
        
for i in range(2, -1, -1):
    if is_number(text[i]):
        num = int(text[i]) + (3-i)
        break

else:
    num = 1

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    
    print("Buzz")
else:
    print(num)