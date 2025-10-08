# Last updated: 2025/10/8 12:15:28
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        def dfs(i, j):
            for dire in directions:
                ni = i + dire[0]
                nj = j + dire[1]
                if ni >= 0 and nj >= 0 and ni < m and nj < n and grid[ni][nj] == "1" and ni * n + nj not in visited:
                    visited.add(ni * n + nj)
                    dfs(ni, nj)
        count = 0
        for step in range(m * n):
            i = int(step / n)
            j = step % n
            if step not in visited and grid[i][j] == "1":
                visited.add(step)
                dfs(i, j)
                count += 1
        return count

                        
                    
        