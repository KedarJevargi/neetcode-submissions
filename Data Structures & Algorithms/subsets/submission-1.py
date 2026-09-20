class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def solve(nums,temp_arr,i,ans):
            if i>=len(nums):
                ans.append(list(temp_arr))
                return

            temp_arr.append(nums[i])
            solve(nums,temp_arr,i+1,ans)
            temp_arr.pop() 
            solve(nums,temp_arr,i+1,ans)  

        solve(nums,[],0,ans)     
        return ans
        