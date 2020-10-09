class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = str(x)
        m = len(new_x)
        result=False
        for i in range(m):
            if new_x[i]==new_x[m-i-1]:
                result=True
            else:
                result=False
                break
        return result
    
    # use no string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
        return False
        z = x
        rev = 0
        while x > 0:
            rem = x % 10
            x = x // 10
            rev = rev * 10 + rem
        return rev == z
