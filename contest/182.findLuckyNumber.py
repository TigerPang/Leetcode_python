class Solution:
    def findLucky(self, arr) -> int:
        d = {}
        lucky = -1
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for i in d.keys():
            if d[i] == i:
                lucky = max(lucky, i)

        return lucky
  
        
def main():

    arr = [2,2,3,3,3]


    ret = Solution().findLucky(arr)
    out = (ret);
    print(out)


if __name__ == '__main__':
    main()
