class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]



        def solve(nums,temp_arr,temp_sum,i,ans,target):
            if i>=len(nums)or temp_sum>target:
                return
            if temp_sum==target:
                ans.append(list(temp_arr))
                return


            temp_arr.append(nums[i])
            solve(nums,temp_arr,temp_sum+nums[i],i,ans,target)
            temp_arr.pop()
            solve(nums,temp_arr,temp_sum,i+1,ans,target)

        solve(nums,[],0,0,ans,target)
        return ans    



        