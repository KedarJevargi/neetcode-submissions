class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def cal(target, temp_sum):
            # base cases
            if temp_sum == target:
                return 1
            if temp_sum > target:
                return 0

            # memo check
            if temp_sum in memo:
                return memo[temp_sum]

            # recursive computation
            memo[temp_sum] = (
                cal(target, temp_sum + 1) +
                cal(target, temp_sum + 2)
            )
            return memo[temp_sum]

        return cal(n, 0)