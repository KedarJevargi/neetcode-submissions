class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        small = 5001  

        while l <= r:
            mid = (l + r) // 2

           
            if nums[l] <= nums[mid]:
                small = min(small, nums[l])
                l = mid + 1
            else:  
                small = min(small, nums[mid])
                r = mid - 1

        return small
