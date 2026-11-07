class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1

        for i in nums:
            if d[i]>2:
                return False


        else:
            return True

        
        
       



        


        
        