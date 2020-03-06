class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < -2 ** 31 or x > 2 ** 31:
            return 0
        
        sym = 1
        
        if x < 0:
            sym = -1
            
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
            
        return res * sym
                
if __name__ == '__main__':
    print(Solution().reverse(123))

    """
        Time Complexity: O(log(x)). There are roughly  log10(x) digits in x.
        Space Complexity = O(1)
 
        Given a 32-bit signed integer, reverse digits of an integer.

        Example:
        Input: 123
        Output: 321
    """
