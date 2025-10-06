# Last updated: 2025/10/6 16:52:06
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # Like rotten oranges problem
        # First, classify two sets of verts by 0/1
        # Second, no need to actually build graph,
        # instead, using directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        # Finally, calculate distance using BFS
        set_0 = deque()
        m = len(mat)
        n = len(mat[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    set_0.append((i, j, 0))
                    res[i][j] = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while set_0:
            u, v, dis = set_0.popleft()
            for dire in directions:
                nu = u + dire[0]
                nv = v + dire[1]
                if nu >= 0 and nu < m and nv >= 0 and nv < n:
                    if mat[nu][nv] == 1:
                        mat[nu][nv] = 0
                        if res[nu][nv] == -1:
                            res[nu][nv] = dis + 1
                        else:
                            res[nu][nv] = min(dis + 1, mat[nu][nv])
                        set_0.append((nu, nv, dis + 1))
        return res

        