class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
the first solution is much faster than the second, it is almost O(n) I think
the time complexity second one is O(n^2)
'''
##        if len(s)==0:
##            return s
##        maxLen=1
##        start=0
##        for i in range(len(s)):
##        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
##        		start=i-maxLen-1
##        		maxLen+=2
##        		continue
##
##        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
##        		start=i-maxLen
##        		maxLen+=1
##        return s[start:start+maxLen]
        palindrome = ''
        
        for i in range(len(s)):
            len1 = len(self.getThePalindrome(s, i, i))
            if len(palindrome) < len1:
                palindrome = self.getThePalindrome(s, i, i)

            len2 = len(self.getThePalindrome(s, i, i + 1))
            if len(palindrome) < len2:
                palindrome = self.getThePalindrome(s, i, i + 1)
        return palindrome
    def getThePalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]



def main():

    L = ["abcbaa", "aaaaaaaaaab", "asdjhqwiehuahksdhabcba", "", "aa", "abb"]
    print("the max sub string in the list are: ")
    for i in L:
        ret = Solution().longestPalindrome(i)
        out = (ret);
        print(out)


if __name__ == '__main__':
    main()
