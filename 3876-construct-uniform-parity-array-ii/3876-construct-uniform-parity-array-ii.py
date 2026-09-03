class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return all( x%2==0 for x in nums1) or all( x%2==1 for x in nums1) or min(nums1)%2==1


        