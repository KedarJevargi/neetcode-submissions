class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def generate(i, array):
            if i >= len(nums):
                ans.append(array.copy())
                return

            array.append(nums[i])
            generate(i + 1, array)

            array.pop()
            generate(i + 1, array)

        generate(0, [])

        return ans




        