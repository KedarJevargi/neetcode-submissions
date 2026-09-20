from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()  

        def solve(i, temp_arr, temp_sum):
            if temp_sum == target:
                ans.append(list(temp_arr))
                return
            if temp_sum > target or i >= len(candidates):
                return

            for j in range(i, len(candidates)):
               
                if j > i and candidates[j] == candidates[j - 1]:
                    continue


                if temp_sum + candidates[j] > target:
                    break

                temp_arr.append(candidates[j])
                solve(j + 1, temp_arr, temp_sum + candidates[j])  
                temp_arr.pop()

        solve(0, [], 0)
        return ans
