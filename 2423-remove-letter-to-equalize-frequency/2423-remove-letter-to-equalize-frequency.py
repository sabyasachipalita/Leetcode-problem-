class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter

        n=len(word)
        for i in range(n):
            sub=word[0:i]+word[i+1:]
            p=Counter(sub).values()
            q=set(p)

            if len(q)==1:
                return True



           


        else:
            return False
        