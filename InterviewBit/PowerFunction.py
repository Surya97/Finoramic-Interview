class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        res = 1
        if x == 0:
            return 0
        
        elif n == 0:
            return 1
        
        elif x == 1:
            return 1
            
        while( n > 0):
            if n%2 == 1:
                res = (res*x)%d
            
            x = (x*x)%d
            
            n/=2
            
        return res
