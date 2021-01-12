from functools import lru_cache


@lru_cache(maxsize=None)
def smallestNumber(n):
   if n == 2000:
       return 121
   prevSum = smallestNumber(n - 1)
   sum = 0
   while prevSum:
       sum += prevSum % 10
       prevSum = prevSum // 10
   return pow(sum + 1, 2)



print(smallestNumber(2020))