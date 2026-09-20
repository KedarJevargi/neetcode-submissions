from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 1:
            return [[strs[0]]]
        
        visited = [False] * n
        ans = []
        
        for i in range(n):
            if visited[i]:
                continue
            ans1 = []
            sorted_string = ''.join(sorted(strs[i]))
            ans1.append(strs[i])
            visited[i] = True
            for j in range(i + 1, n):
                if not visited[j] and sorted_string == ''.join(sorted(strs[j])):
                    ans1.append(strs[j])
                    visited[j] = True
            ans.append(ans1)
        
        return ans
