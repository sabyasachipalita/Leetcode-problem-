class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={}
        vowels='aeiou'
        for i in s:
            d[i]=d.get(i,0)+1


        for k in d:
            p=max(( v for k,v in d.items() if k in vowels),default=0)


            q=max(( v for k,v in d.items() if k not in vowels),default=0)

        return p+q
           
        

        


        
        