class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        j=0
        p=set()
        for i in range(len(s)):
            while s[i] in p:
                p.remove(s[j])
                j+=1

            p.add(s[i])
            ans=max(ans,i-j+1)


        return ans 

            



        