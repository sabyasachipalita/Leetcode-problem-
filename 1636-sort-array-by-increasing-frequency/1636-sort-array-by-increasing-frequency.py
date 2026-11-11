class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        d={}
        q=[]
        for i in nums:
            d[i]=d.get(i,0)+1

        
        p=sorted(d.items(),key=lambda x:(x[1],-x[0]) )
            

        for a,b in p:
                q.extend([a]*b)

        return q



        # (1,2) (2,3)(3,1)

             


        