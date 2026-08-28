class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l=0
        ans=0
        d={0:-1}
        c=0
        ans=0
        for r in range(len(nums)):
            if nums[r]==1:
                c+=1
            else:
                c-=1

            if c in d:
                ans=max(ans,r-d[c])


            else:
                d[c]=r

        return ans 


     


        