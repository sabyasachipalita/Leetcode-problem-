class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr)==1 or len(arr)==2:
            return False


        else:
            for i in range(1,len(arr)-1):
                if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    peak=arr[i]
                    left=i
                    right=i

                    while left>0 and arr[left]>arr[left-1]:
                        left-=1

                    while right <len(arr)-1 and arr[right]>arr[right+1]:
                        right+=1

                    
                    if left==0 and right==len(arr)-1:
                        return True

                    else:
                        return False

            else:
                    return False

         


                    


                    

           


            # for i in range(1,len(arr)):
            #     if arr[i]==arr[i-1]:
            #         return False

            #     elif arr[i]<arr[i-1]:
            #         return False


            # else:
            #     return True





        