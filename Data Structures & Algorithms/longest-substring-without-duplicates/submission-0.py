class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0    

        res = 0
        left, right = 0, 0
        hashmap = {}

        while right < len(s):
            if s[right] not in hashmap or hashmap[s[right]] == 0:
                hashmap[s[right]] = 1
                res = max(res, right - left + 1)
                right += 1
            else:
                hashmap[s[left]] -= 1
                left += 1

        return res