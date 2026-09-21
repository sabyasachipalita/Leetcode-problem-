class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        d={}
        d1={}

        for i in range(len(s)):
            p=s[i]
            q=t[i]

            if p in d:
                if d[p]!=q:
                    return False


            d[p]=q


            if q in d1:
                if d1[q]!=p:
                    return False



            d1[q]=p

        return True
        