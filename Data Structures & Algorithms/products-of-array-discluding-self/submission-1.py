class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count=nums.count(0)
        n=len(nums)
        ans=[]

        if zero_count>1:
            return [0]*n

        


        if zero_count==1:
            prod=1
            for i in nums:
                if i!=0:
                    prod*=i
            for i in nums:
                if i!=0:
                    ans.append(0)
                else:
                    ans.append(prod)   
        else:
            prod=1
            for i in nums:
                prod*=i
            for i in nums:
                ans.append(prod//i)    


        return ans                 
        