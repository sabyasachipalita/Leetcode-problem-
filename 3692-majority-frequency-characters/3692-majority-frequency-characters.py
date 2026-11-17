class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1


        p={}
        
        for i,j in d.items():
            p.setdefault(j,[]).append(i)


        max_len=0
        max_gr=[]
        max_fre=0
        for j,k in p.items():
            if (len(k)>max_len):
                max_len=len(k)
                max_gr=k
                max_fre=j

            elif  max_len==len(k) and j>max_fre:
                max_fre=j
                max_gr=k

        return ''.join(max_gr)


        

        

        

        


        

            

        