from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:
            check = str(sorted(Counter(word).items()))

            if check not in mp:
                mp[check] = [word]
            else:
                mp[check].append(word)

        return list(mp.values())