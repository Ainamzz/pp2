import math
def multiply(n):
    return math.prod(n)
nums = list(map(int, input("Enter numbers:").split()))
result = multiply(nums)
print(result)