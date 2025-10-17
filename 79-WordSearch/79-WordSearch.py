# Last updated: 2025/10/16 18:11:09
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        queue = deque()
        # find index of initial letter
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    queue.append((i, j))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # up, down, left, right
        def dfs(node, depth):
            if depth == len(word):
                return True
            i, j = node
            for dire in directions:
                ni = i + dire[0]
                nj = j + dire[1]
                if ni < m and ni >= 0 and nj < n and nj >= 0 and (ni, nj) not in states:
                    if board[ni][nj] == word[depth]:
                        states.add((ni, nj))
                        if dfs((ni, nj), depth + 1):
                            return True
                        else:
                            states.remove((ni, nj))
            return False
                    
        while queue:
            # here using set instead of list
            # because search in list is O(N)
            # but search in set is O(1)
            states = set()
            i, j = queue.popleft()
            states.add((i, j))
            if dfs((i, j), 1):
                return True
        return False

        