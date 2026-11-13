class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1


        even={k:v for k,v in d.items() if k%2==0}
        if not even:
            return -1


        ans=max(even.items(),key=lambda x:(x[1],-x[0]))
        return ans[0]
        

        

     
        


       

        