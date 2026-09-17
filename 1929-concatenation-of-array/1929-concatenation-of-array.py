class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums
        n=len(nums)
        for i in range(n):
            ans.append(nums[i])


        return ans 
       
        # n=len(nums)
        # ans=[1]*(2*n)
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]==0:
        #         ans[i]=0

        #     else:
                

        