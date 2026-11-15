class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        ans=[]
        for i in range(len(s)):
            if s[i]==c:
                ans.append(i) 


        p=[]

        for j in range(len(s)):
            mini=float("inf")

            for i in ans:
                mini=min(mini,abs(j-i))
            p.append(mini)


        return p





        