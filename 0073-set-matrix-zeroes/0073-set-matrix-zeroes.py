class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                 if matrix[i][j] == 0:
                        rows.add(i)
                        cols.add(j)
        
        for r in rows:
            matrix[r] = [0]*len(matrix[0])
            
        
        for c in cols:
            for k in range(len(matrix)):
                matrix[k][c] = 0
        