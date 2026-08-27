class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r=''
        n=len(indices)
        for i in range(n):
            r=r+s[indices.index(i)]

        return r
     


    
      
        