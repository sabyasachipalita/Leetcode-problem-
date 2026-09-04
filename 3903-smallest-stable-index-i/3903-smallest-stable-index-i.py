class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
      
        # if k==0:
        #     return 0
        for i in range(len(nums)):
            min_val=max(nums[0:i+1])-min(nums[i:len(nums)])
            if min_val<=k:
                return i
           

        else:
            return -1

        