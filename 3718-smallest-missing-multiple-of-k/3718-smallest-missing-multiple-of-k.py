class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        p=k
        
        for x in nums:
            if k not in nums:
                return k

            else:
                k=k+p
        return k
                

        


            
                


        