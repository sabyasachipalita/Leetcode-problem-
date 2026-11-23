class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        p=[]
        n=[]
        r=[]
        for i in nums:
            if i>0:
                p.append(i)

            else:
                n.append(i)

        for j in range(len(p)):
            r.append(p[j])
            r.append(n[j])

        return r

        
        