class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1

       #(1-1  2-1  3-1  4-2 5-1)
        p=[ v for k,v in d.items()]

        for i in p:
            if i<2:
                continue

            is_prime=True

            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    is_prime=False
                    break
            if is_prime:
                    return True

        return False


            

                





            
        


        