class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        d={}
        for x in  range(len(nums)-1):
            if nums[x]==key:
                target=nums[x+1]

                d[target]=d.get(target,0)+1

        p=max(d,key=d.get)
        return p


        
                

            


      

        
        