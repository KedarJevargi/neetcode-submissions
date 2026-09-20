
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(time):
            count=0
            for i in piles:
                count+=math.ceil(i/time)
            return count<=h    
                
        max_pile=max(piles)
        l=1
        r=max_pile-1
        
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                r=mid-1
            else:
                l=mid+1 
        return l         
            
    