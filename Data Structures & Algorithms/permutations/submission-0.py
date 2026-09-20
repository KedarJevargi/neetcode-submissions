class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        visited=[0]*len(nums)

        def solve(nums,temp_arr,visited,ans):
            if len(temp_arr)==len(nums):
                ans.append(list(temp_arr))
                return



            for i in range(len(nums)):
                if visited[i]==0:
                    visited[i]=1
                    temp_arr.append(nums[i])
                    solve(nums,temp_arr,visited,ans)
                    visited[i]=0
                    temp_arr.pop()
        solve(nums,[],visited,ans)     
        return ans       

                    

                    




        