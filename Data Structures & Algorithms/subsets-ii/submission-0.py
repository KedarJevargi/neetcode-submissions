class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        ans = []

        def cal(nums, arr, i):
            if i >= len(nums):
                key = tuple(arr)
                if key not in seen:
                    ans.append(list(arr))
                    seen.add(key)
                return

            arr.append(nums[i])
            cal(nums, arr, i + 1)
            arr.pop()
            cal(nums, arr, i + 1)

        cal(nums, [], 0)
        return ans
