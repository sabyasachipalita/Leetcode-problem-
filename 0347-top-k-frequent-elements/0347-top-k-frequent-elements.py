class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        r=[]
        for i in nums:
            d[i]=d.get(i,0)+1

        p=sorted(d.items(), key=lambda x:[x[1]],reverse=True)
        for j,v in p:
            r.append(j)


        return r[:k]



        

        


        