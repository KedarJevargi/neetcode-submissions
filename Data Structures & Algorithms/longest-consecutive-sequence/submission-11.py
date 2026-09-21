class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map=set(nums)
        max_count=0
        if not nums:
            return 0
        for i in map:
            count=0
            if i-1 not in map:
                while i+1 in map:
                    count+=1
                    i+=1
            max_count=max(max_count,count+1)  

        return max_count          

                  










          
           

        