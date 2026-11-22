class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s=0
        for i in range(k):
            p=max(nums)
            s=s+p
            new=p+1
            nums.remove(p)
            nums.append(new)

        return s




        