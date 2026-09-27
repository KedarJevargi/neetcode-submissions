from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map=Counter(nums)

        for key, val in map.items():
            if val>1:
                return key


        