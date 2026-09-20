from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        # Recursive palindrome check
        def check_palindrome(word, l, r):
            if l >= r:
                return True
            if word[l] != word[r]:
                return False
            return check_palindrome(word, l + 1, r - 1)
        
        # Your original recursion logic
        def solve(i, temp_arr):
            if i >= len(s):
                # Add the current partition to answer
                ans.append(temp_arr[:])
                return
            
            # Try partitioning at different positions
            for j in range(i, len(s)):
                word = s[i:j+1]
                if check_palindrome(word, 0, len(word) - 1):
                    temp_arr.append(word)
                    solve(j + 1, temp_arr)
                    temp_arr.pop()
        
        solve(0, [])
        return ans