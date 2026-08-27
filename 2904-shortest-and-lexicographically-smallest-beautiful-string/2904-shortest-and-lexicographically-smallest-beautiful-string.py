class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones=0
        l=0
        p=''
        for r in range(len(s)):
            if s[r]=='1':
                ones+=1
                while l<r and (ones>k or s[l]=='0'):
                    if s[l]=='1':
                        ones-=1
                    l+=1

                   
                if ones==k:
                            ss=s[l:r+1]
                            if (not p or len(ss)<len(p)) or (len(ss)==len(p) and ss<p):
                                p=ss

        return p







                    

                    



                   


                
    
                
                

        