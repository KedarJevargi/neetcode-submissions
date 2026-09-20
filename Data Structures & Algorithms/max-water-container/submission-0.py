class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water=0
        l=0
        r=len(height)-1



        def area(i,j,hi,hj):
            return (j-i)*min(hi,hj)

        while l<r:
            most_water=max(most_water,area(l+1,r+1,height[l],height[r])) 


            #move right
            if height[l]<height[r]:
                l+=1
            #move left
            else:
                r-=1
     

        return most_water        

            

            




        
        