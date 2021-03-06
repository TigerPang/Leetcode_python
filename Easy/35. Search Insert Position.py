class Solution:
    def searchInsert(self, nums, target):
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
#         if target in nums:
#             return nums.index(target)
#         else:
#             for i in nums:
#                 if target > nums[-1]:
#                     return len(nums)
#                 if i > target:
#                     return nums.index(i)
if __name__ == '__main__':
    print(Solution().searchInsert([1,2,3], 6))
    
    
    """
        Time Complexity = O(N)
        Space Complexity = O(1)

        Given a sorted array and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.
        You may assume no duplicates in the array.
        Example:
        Input: [1,3,5,6], 5
        Output: 2
    """
