class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==0:
            return ''

        else:
            base=strs[0] 
            for i in range(len(base)): 
                for j in strs[1:]:
                    if i==len(j) or base[i]!=j[i]:
                        return base[0:i]

            return base

            
            







        