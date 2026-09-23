class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep letters and numbers, then lowercase everything
        sen = "".join([char for char in s if char.isalnum()]).lower()

        l = 0
        r = len(sen) - 1    

        while l < r:
            if sen[l] != sen[r]:
                return False
            l += 1
            r -= 1

        return True
