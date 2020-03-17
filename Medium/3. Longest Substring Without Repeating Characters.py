class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dictionary = {}
        start = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in char_dictionary and char_dictionary[s[i]] >= start:
                start = char_dictionary[s[i]] + 1
                char_dictionary[s[i]] = i
            else:
                char_dictionary[s[i]] = i
                max_length = max(max_length, i - start + 1)
        return max_length

def stringToString(input):
    import json

    return json.loads(input)

def main():           
        ret = Solution().lengthOfLongestSubstring("abcabcbb")
        out = str(ret);
        print(out)


if __name__ == '__main__':
    main()

'''
 Time complexity: O(2n)=O(n). 
'''
