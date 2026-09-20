class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap={}
        n=len(nums)

        for i in range(n):
            if nums[i] not in hashmap:

                hashmap[target-nums[i]]=i
            else:

                return [hashmap[nums[i]],i]    
        