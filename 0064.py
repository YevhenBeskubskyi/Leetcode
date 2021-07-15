# Leetcode 0064 (Medium): Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        data = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    data[i][j] = grid[i][j]
                elif i == 0:
                    data[i][j] = data[i][j-1] + grid[i][j]
                elif j == 0:
                    data[i][j] = data[i-1][j] + grid[i][j]
                else:
                    x = data[i][j-1]
                    y = data[i-1][j]
                    data[i][j] = min(x, y) + grid[i][j]
        
        return data[-1][-1]
