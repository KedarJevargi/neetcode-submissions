from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        map=Counter(nums)
        for key,val in map.items():
            heap.append((-val,key))


        heapq.heapify(heap)  
        ans=[]  

        for i in range(k):
            ans.append((heapq.heappop(heap)[1]))


        return ans     





        