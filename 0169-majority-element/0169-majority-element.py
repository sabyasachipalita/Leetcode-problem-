class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d={}
        max_val=1
        key=None
        for i in nums:
            d[i]=d.get(i,0)+1


        for k in d:
            if d[k]>=max_val:
                max_val=d[k]
                key=k

        return key

    

            



            
        