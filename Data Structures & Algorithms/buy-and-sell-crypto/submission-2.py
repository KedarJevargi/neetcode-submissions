class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        buy=0
        sell=1
        max_profit=0

        while sell<len(prices):
            if prices[buy]>prices[sell]:
                buy+=1
                sell=buy+1
            else:
                max_profit=max(max_profit,prices[sell]-prices[buy])
                sell+=1
        return max_profit            

        