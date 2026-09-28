class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=""
        for i in digits:
            num+=str(i)

        num=str(int(num)+1)    
        ans=[int(i) for i in num]    

        return ans


        
        