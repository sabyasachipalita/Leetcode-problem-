class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn=min(nums)
        r=0
        for i in nums:
            r=r+(i-mn)

        return r
      


  


        