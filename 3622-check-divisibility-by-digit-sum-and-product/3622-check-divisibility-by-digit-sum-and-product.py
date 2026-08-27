class Solution:
    def checkDivisibility(self, n: int) -> bool:
        mul=1
        s=0
        p=n
        total=0
        while (n!=0):
            r=n%10
            mul=mul*r
            s=s+r
            
            n=n//10
        total=s+mul

        

        if p%total==0:
            return True

        else:
            return False




        