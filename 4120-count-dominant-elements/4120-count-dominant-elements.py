class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n=len(nums)
        d_c=0
        for i in range(len(nums)):
            if len(nums)==1:
               return 1

            if i==0:
                if nums[i]>=nums[i+1]:
                    d_c+=1

            elif i==n-1: 
                if nums[i]>=nums[i-1]:
                    d_c+=1  



            else:
                if 2*nums[i]>=(nums[i+1]+nums[i-1]):
                    d_c+=1

        return d_c

             


     



            



        