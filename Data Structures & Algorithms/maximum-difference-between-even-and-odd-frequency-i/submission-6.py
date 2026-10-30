from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        min_even = float('inf')
        max_odd = 0

        for val in freq.values():
            if val % 2 == 0:
                min_even = min(min_even, val)
            else:
                max_odd = max(max_odd, val)

        return max_odd - min_even