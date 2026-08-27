class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            c=0
            while nums[i]!=-1:
                c+=1
                nums[i],i=-1,nums[i]

                ans=max(ans,c)

        return ans
        