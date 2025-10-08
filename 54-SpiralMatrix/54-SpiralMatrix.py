# Last updated: 2025/10/7 17:27:43
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # right, down, left, up
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        i = 0
        j = 0
        dir_i = 0
        step = 0
        m = len(matrix)
        n = len(matrix[0])
        bool_m = [[0 for _ in range(n)] for _ in range(m)]
        while step < m * n:
            res.append(matrix[i][j])
            bool_m[i][j] = -1
            ni = i + directions[dir_i % 4][0]
            nj = j + directions[dir_i % 4][1]
            if ni < 0 or nj < 0 or ni >= m or nj >= n or bool_m[ni][nj] == -1:
                dir_i += 1
            i += directions[dir_i % 4][0]
            j += directions[dir_i % 4][1]
            step += 1
        return res
                
        