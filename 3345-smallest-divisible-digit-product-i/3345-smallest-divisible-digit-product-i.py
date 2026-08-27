class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
          temp=n
          product=1
          while temp>0:
            r=temp%10
            product=product*r
            temp=temp//10
          if product%t==0:
                return n

          n+=1

          
        
      


        
        
        