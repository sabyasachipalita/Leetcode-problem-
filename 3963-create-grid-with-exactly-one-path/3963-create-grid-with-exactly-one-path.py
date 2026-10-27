class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # m=col,n=row
        grid=[['#']*n for _ in range(m)]
        for i in range(m):
            grid[i][0]='.'
            

        for j in range(n):  # 0 1 2 
            grid[-1][j]='.'

        return [''.join(r) for r in grid]

            
            


       
        