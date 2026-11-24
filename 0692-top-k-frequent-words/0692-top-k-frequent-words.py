class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d={}
        r=[]
        for x in words:
            d[x]=d.get(x,0)+1


        p=sorted(d.items(),key=lambda x :(-x[1],x[0]))[0:k]

        for a,b in p:
            r.append(a)

        return r


    


        