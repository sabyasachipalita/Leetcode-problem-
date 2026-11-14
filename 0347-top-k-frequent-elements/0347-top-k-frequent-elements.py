class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        p=[]
        for i in nums:
            d[i]=d.get(i,0)+1


        top=sorted(d,key=d.get,reverse=True)
        return top[0:k]




        


        


        

        