class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s)
        r=0
        for i in range(0,len(s)-1,2):
            if s[i]!=s[i+1]:
                r+=1

        return r


        