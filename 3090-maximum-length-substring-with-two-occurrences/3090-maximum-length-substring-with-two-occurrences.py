class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        n=len(s)
        ans=0
        d={}
        for right in range(n):
            d[s[right]]=d.get(s[right],0)+1

            while l<right and d[s[right]]>2:
                d[s[l]]-=1
                l+=1
            ans=max(ans,right-l+1)
        return ans 

        