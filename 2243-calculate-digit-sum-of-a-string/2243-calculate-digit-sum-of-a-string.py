class Solution:
    def digitSum(self, s: str, k: int) -> str:


        if  not s:
            return ''

        else:
            while len(s)>k:
                ans=[]
                for i in range(0,len(s),k):
                    a=s[i:i+k]

                    ans_val=0
                    for i in a :
                       ans_val+=int(i)


                    ans.append(str(ans_val))

                s=''.join(ans)
            return s

            

           


           



      
       

            



            

            

            


            

             



   


        