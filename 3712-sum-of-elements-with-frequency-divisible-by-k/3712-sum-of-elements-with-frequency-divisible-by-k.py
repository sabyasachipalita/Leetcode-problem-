class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1

        p=[ j*v for j,v in d.items() if v%k==0 ]
        return sum(p)


        



        