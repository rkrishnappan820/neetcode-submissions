class Solution:
    def myPow(self, x: float, n: int) -> float:
       if n > 0:
            times_multiplied = n - 1
            total = x
       elif n < 0:
            times_multiplied = abs(n) - 1
            total = 1/x
            x = 1/x
       else: 
            return 1.0
            
       while times_multiplied > 0:
            total *= x
            times_multiplied -= 1
       return total
        
