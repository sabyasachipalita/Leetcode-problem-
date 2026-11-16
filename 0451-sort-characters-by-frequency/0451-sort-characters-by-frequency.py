class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        r=''
        for i in s:
            d[i]=d.get(i,0)+1

        p=sorted(d.items(),key=lambda x :x[1],reverse=True)
        for a,b in p:
            r=r+(b*a)

        return r



        

        