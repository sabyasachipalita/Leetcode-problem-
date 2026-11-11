class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        ans=0
        p=str(n)
        for i in range(len(p)):
            d[p[i]]=d.get(p[i],0)+1

        for k in d:
            ans+=(int(d[k])*int(k))


        return ans 

        