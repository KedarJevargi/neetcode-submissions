class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

    
        if 0 in freq and freq[0] > 1:
            return [0] * len(nums)


        if 0 in freq and freq[0] == 1:
            zprod = 1
            for x in nums:
                if x != 0:
                    zprod *= x
            ans = []
            for x in nums:
                if x == 0:
                    ans.append(zprod)
                else:
                    ans.append(0)
            return ans


        prod = 1
        for x in nums:
            prod *= x

        ans = []
        for x in nums:
            ans.append(prod // x) 
        return ans
