class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        p=[0]*len(nums)
        n=len(nums)
        
        for i in range(len(nums)):
            if nums[i]==0:
                p[i]=0
                

            else:
                p[i]=nums[(i+nums[i])%n]

               

        return p
        