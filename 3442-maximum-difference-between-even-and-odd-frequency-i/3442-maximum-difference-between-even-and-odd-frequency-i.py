class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1

        odd= [ v for k,v in d.items() if v%2!=0]
        even=[v for k,v in d.items() if v%2!=1]

        return max(odd)- min(even)


        