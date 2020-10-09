class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x<0 else 1
        y=abs(x)
        while y!=0:
            rem = y%10
            rev = rev*10+rem
            y = y//10
        result=int(sign*rev)
        return 0 if result<((-2)**31) or result>(2**31-1) else result
