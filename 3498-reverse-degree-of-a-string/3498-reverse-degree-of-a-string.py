class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            ch=26-(ord(s[i])-ord("a"))
            ind=ch*(i+1)
            ans=ans+ind

        return ans 


        