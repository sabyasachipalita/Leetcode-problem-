class Solution:
    def magicalString(self, n: int) -> int:
        if n<=3:
            return 1

        else:
             
            p=[1,2,2]   # 1,2,2,1,1,2,1,2,2,1,2,2
            num=1 # 2
            i=2 
            while len(p)<n: #6
                count=p[i]
                for _ in range(count):  
                  if len(p)==n:
                      break

                  p.append(num)

                num=3-num
                i+=1


            return p[0:n].count(1)







       

    





        

        