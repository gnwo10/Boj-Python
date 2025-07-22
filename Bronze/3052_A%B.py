import sys

input = sys.stdin.readline
result = []

for _ in range(10):
    a = int(input())
    result.append(a % 42)

count = 0
nums = []

for i in result:
    if i not in nums:
        nums.append(i)

    
print(len(nums))



