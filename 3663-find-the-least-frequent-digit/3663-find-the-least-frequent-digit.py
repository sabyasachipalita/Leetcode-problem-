class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        p=str(n)
        d={}
        for i in p:
            d[i]=d.get(i,0)+1


        s=min(d.items(),key=lambda x:(x[1],int(x[0])))

        return int(s[0])




      




        