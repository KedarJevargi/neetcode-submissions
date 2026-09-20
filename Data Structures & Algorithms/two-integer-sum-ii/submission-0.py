class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(array,l,r,target):
            while l<=r:
                mid=(l+r)//2
                if array[mid]==target:
                    return mid
                elif array[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return -1

        for i in range(len(numbers)):
            l=0
            r=len(numbers)-1
            target_idx=search(numbers,l,r,target-numbers[i])
            if target_idx!=-1:
                return [i+1,target_idx+1] 

                                 
        