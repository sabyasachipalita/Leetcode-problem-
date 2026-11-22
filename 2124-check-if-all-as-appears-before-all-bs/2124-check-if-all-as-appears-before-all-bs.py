class Solution:
    def checkString(self, s: str) -> bool:
        seenb=False

        for x in s:
            if x=='b':
                seenb=True

            elif x=='a'  and seenb==True:
                return False


        else:
            return True



        

      
    



        

        