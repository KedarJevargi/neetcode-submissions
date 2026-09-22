class Solution:
    def __init__(self):
            self.dp={}
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            if n in self.dp:
                return self.dp[n]    
            else:
                self.dp[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
                return self.dp[n]



        