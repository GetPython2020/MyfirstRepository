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
