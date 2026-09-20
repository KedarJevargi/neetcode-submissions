class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {"(": ")", "{": "}", "[": "]"}
        
        for ch in s:
            if ch in hash_map: 
                stack.append(hash_map[ch]) 
            else:  
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()
                
        return not stack 
