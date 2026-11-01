class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_window_map={}
        n=len(s)
        max_len=0
        l,r=0,0


        while r<n:
            if s[r] not in current_window_map or current_window_map[s[r]]==0:
                max_len=max(max_len,(r-l)+1)
                current_window_map[s[r]]=1

                r+=1
            else:
                current_window_map[s[l]]-=1
                l+=1



        return max_len        
                






        