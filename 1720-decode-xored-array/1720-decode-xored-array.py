class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        p=[]
        p.append(first)
        
        for i in range(len(encoded)):
            p.append(p[i]^encoded[i])
            
            

        return p



            

        