class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        
        
        for i in range(0, 9):
            rows = dict()
            cols = dict()
            cube = dict()
            for j in range(0, 9):
                if A[i][j]!='.':
                    if (A[i][j] in rows):
                        return 0
                    else:
                        rows[A[i][j]] = 1
                
                if A[j][i] !='.':
                    if (A[j][i] in cols):
                        return 0
                    else:
                        cols[A[j][i]] = 1
                        
                t1 = 3*(i/3)
                t2 = 3*(i%3)
                
                if A[t1+j/3][t2+j%3]!='.':
                    if (A[t1+j/3][t2+j%3] in cube):
                        return 0
                    else:
                        cube[A[t1+j/3][t2+j%3]] = 1
                        
        return 1
                    
                
                    
                
                
            
