from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq_map = {}
        
       
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

       
        max_heap_items = [(-freq, num) for num, freq in freq_map.items()]
        heapq.heapify(max_heap_items)

     
        for _ in range(k):
            ans.append(heapq.heappop(max_heap_items)[1])

        return ans
