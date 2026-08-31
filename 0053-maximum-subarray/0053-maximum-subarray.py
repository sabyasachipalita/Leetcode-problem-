class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=0
        k=0
        for x in nums:
            k=k+x
            ans=max(ans,k)
            if k<0:
                k=0

        return ans

        