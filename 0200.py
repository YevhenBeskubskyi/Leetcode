def bfs(i, j, grid):
    if i < 0 or i >= len(grid):
        return
    if j < 0 or j >= len(grid[i]):
        return
    if grid[i][j] == '0':
        return
    grid[i][j] = '0'
    bfs(i+1, j, grid)
    bfs(i-1, j, grid)
    bfs(i, j+1, grid)
    bfs(i, j-1, grid)

def num_of_islands(grid):
    '''
    Leetcode 0200 (Medium): Number of Islands
    '''
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                count += 1
                bfs(i, j, grid)
    return count
