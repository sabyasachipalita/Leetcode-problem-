class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        ans=0
        n=len(nums)
        for i in range(n):
            p=[]
            for j in range(i,n):
                p.append(nums[j])

                if all( p[k]>p[k-1] for k in range(1,len(p))) or all( p[k]<p[k-1] for k in range(1,len(p))):
                    ans=max(ans,j-i+1)


        return ans 

                

        

        