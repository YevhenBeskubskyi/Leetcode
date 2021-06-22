def unique_paths(m, n):
    '''
    Leetcode 0062 (Medium): Unique Paths
    https://leetcode.com/problems/unique-paths/
    '''
    grid = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            x = grid[i-1][j]
            y = grid[i][j-1]
            grid[i][j] = x + y
    return grid[-1][-1]
