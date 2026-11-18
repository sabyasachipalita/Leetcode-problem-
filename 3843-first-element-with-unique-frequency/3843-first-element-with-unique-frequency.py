class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1

        # 20-1 10-1 30-2

        p= [v for k,v in d.items()]
        q={}
        for j in p:
            q[j]=q.get(j,0)+1

        l=[ a for a,b in d.items() if q[b]==1]
        return l[0] if l else -1
        



        
        

        