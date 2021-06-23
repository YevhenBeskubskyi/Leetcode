# Leetcode 0200 (Medium): Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[i]):
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            
            bfs(i+1, j)
            bfs(i-1, j)
            bfs(i, j+1)
            bfs(i, j-1)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count
