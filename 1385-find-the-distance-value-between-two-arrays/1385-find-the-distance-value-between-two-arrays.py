class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n=len(arr1)
        m=len(arr2)
        c=0
        for i in range(n):
            found=False

            for j in range(m):
                if abs(arr1[i]-arr2[j])<=d:
                    found=True
                    break

            
            if found==False:
                   c+=1

        return c



        