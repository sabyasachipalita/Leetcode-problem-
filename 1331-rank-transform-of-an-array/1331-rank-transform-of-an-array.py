class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        p=arr[:]
        result=[]
        arr.sort()
        d={}
        rank=1
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=rank
                rank+=1


        for k in p:
            result.append(d[k])


        return result



            



    


        

        