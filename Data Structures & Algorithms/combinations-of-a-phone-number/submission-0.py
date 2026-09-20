class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        hashmap={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        ans=[]

        def solve(digits,i,temp_arr,ans):

            if i>=len(digits):
                ans.append("".join(list(temp_arr)))
                return

            arr=hashmap[digits[i]]
            
            for j in arr:
                temp_arr.append(j)
                solve(digits,i+1,temp_arr,ans)
                temp_arr.pop()

        solve(digits,0,[],ans)  
        return ans  
            

        
        