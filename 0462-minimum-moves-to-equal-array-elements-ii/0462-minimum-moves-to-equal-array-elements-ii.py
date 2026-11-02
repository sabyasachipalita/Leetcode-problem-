class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        r=0
        nums.sort()
        for i in nums:
            mid_val=n//2
            val=abs(i-nums[mid_val])
            r=r+val

        return r

        # 1 2 9 10


    

        