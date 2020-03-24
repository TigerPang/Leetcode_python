class Solution:
    ''' Time complexity: 4^N
'''
    def letterCombinations(self, digits):
        digit_map = {2:"abc", 
                     3:"def", 
                     4:"ghi", 
                     5:"jkl", 
                     6:"mno", 
                     7:"pqrs", 
                     8:"tuv", 
                     9:"wxyz"}
        # solution1 dfs:
        if len(digits) == 0:
            return []
        result = []
        def dfs(digits, index, temp):
            if len(digits) == len(temp):
                result.append("".join(temp))
                return
            for char in digit_map[int(digits[index])]:
                temp.append(char)
                dfs(digits, index + 1, temp)
                temp.pop()
        dfs(digits, 0, [])
        return result
        
        # solution2
        # if len(digits) == 0:
        #     return []
        # result = ['']
        # length = len(digits)
        # for digit in digits:
        #     temp = []
        #     for char in digit_map[int(digit)]:
        #         for s in result:
        #             temp.append(s + char)
        #     result = temp
        # return result
def main():

    L = ["23", "234", "34", "", "35", "66"]
    print("the combinations for each strings are: ")
    for i in L:

        ret = Solution().letterCombinations(i)
        out = (ret);
        print(out)


if __name__ == '__main__':
    main()
