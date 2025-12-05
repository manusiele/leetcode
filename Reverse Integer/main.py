class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Overflow check
            if sign == 1:
                if rev > 2147483647 // 10 or (rev == 2147483647 // 10 and pop > 7):
                    return 0
            else:
                if rev > 2147483648 // 10 or (rev == 2147483648 // 10 and pop > 8):
                    return 0
                
            rev = rev * 10 + pop
            
        return sign * rev