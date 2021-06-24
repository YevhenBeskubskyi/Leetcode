# Leecode 0051 (Hard): N-Queens
# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        
        col = set()
        posDiag = set()
        negDiag = set()
        
        def backtrack(r):
            if r == n:
                copy = [''.join(r) for r in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or r - c in negDiag or r + c in posDiag:
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                
                backtrack(r + 1)
                
                board[r][c] = '.'
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                
        backtrack(0)
        return res
            
