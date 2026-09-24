class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        
        for i in range(len(nums)):
            s=0
            while nums[i]>0:
                s=s+(nums[i]%10)
                nums[i]=nums[i]//10


            if i==s:
                return i

      
        return -1

            

                
                    

                



            



        