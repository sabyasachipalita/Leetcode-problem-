class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr=[0]*1001
        res=[]

        for x in arr1:
            arr[x]=arr[x]+1

        

        for j in arr2:
            while arr[j]>0:
                res.append(j)
                arr[j]-=1

        for i in range(1001):

           while arr[i]>0:
              res.append(i)
              arr[i]-=1

        return res

        