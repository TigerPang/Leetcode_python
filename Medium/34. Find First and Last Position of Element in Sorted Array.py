class Solution:
'''
Time complexity: O(logn) because using binary search
Space complexity: O(1) because all work is done in place,
so the overall memory usage is constant
'''
    def position(self, nums, target, length):
        index = length
        start = 0
        end = length - 1
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] >= target:
                index = mid
                end = mid - 1
            else:
                start = mid + 1
        return index
    def searchRange(self, nums, target):
        length = len(nums)
        if length == 0 or nums == None:
            return [-1, -1]
        index1 = self.position(nums, target, length)
        index2 = self.position(nums, target + 1, length) - 1
        if index1 <= index2:
            return[index1, index2]
            
        else:
            return [-1, -1]


def main():
    nums = [5, 6, 6, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10]
    targets = [8, 6, 0]
    for target in targets:
        
        ret = Solution().searchRange(nums, target)
        print(ret)


if __name__ == '__main__':
    main()
