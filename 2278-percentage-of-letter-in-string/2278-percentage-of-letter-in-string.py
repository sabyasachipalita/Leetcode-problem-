class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n=len(s)
        a=s.count(letter)
        

        final_result=(a*100)/(n)
        return floor(final_result)
        

        