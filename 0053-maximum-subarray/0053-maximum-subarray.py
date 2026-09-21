class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        k=0
        for x in nums:
            k=k+x
            ans=max(ans,k)
            if k<0:
                k=0

        return ans

        