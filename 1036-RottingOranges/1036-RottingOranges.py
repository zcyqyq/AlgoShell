# Last updated: 2025/10/6 16:24:28
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        verts = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    verts.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_t = 0
        while verts:
            vert = verts.popleft()
            u, v, t = vert
            max_t = max(max_t, t)
            for dire in directions:
                nu = u + dire[0]
                nv = v + dire[1]
                if nu >= 0 and nv >= 0 and nu < m and nv < n:
                    if grid[nu][nv] == 1:
                        grid[nu][nv] = 2
                        verts.append((nu, nv, t + 1))
                        fresh -= 1
        if fresh == 0:
            return max_t
        else:
            return -1