class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        l = []  
        sign = 1 if num >= 0 else -1
        num = abs(num) 
        while num > 0:
            l.append(str(num % 7))
            num //= 7 
        result = ''.join(reversed(l))
        return '-' + result if sign == -1 else result
