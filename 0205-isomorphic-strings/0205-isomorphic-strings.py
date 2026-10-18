class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        p=[]
        for i in s:
            p.append(s.index(i))

        q=[]
        for j in t:
            q.append(t.index(j))


        return p==q
        