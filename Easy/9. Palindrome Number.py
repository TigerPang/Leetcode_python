class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        
        return x == revertedNumber or x == revertedNumber // 10
    
    '''
        The idea is to check if thei first half of the x is equal to the           second half of the x. If they are the same, then the number is a           palindrome.
    
        Time complexity: O(log10(n)). We divided the input by 10 for every         iteration, so the time complexity is O(log10(n)) 
        Space complexity: O(1)
    
    '''
        # Solution 2:
        # slower, cos need to reverse all digits
        # copyX = x
        # revertedNumber = 0
        # while copyX != 0:
        #     revertedNumber = revertedNumber * 10 + copyX % 10
        #     copyX //= 10
        # if revertedNumber == x:
        #     return True
        # return False

def main():
    L = [1221, 121, 1234, -123, -1221, 3333, 2222, 1111]
    for i in L:      
        ret = Solution().isPalindrome(i)

        out = (ret);
        print(out)


if __name__ == '__main__':
    main()
