class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
        while l<=r:
            width=min(height[l],height[r])
            length=r-l
            area=width*length
            ans=max(ans,area)

            if height[l]<height[r]:
                l+=1

            else:
                r-=1

        return ans

        