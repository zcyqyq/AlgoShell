# Last updated: 2025/10/16 17:30:52
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = set()
        res = []
        queue = deque()
        queue.append([])
        visited.add(frozenset([]))
        while queue:
            node = queue.popleft()
            for num in nums:
                if num in node:
                    continue
                node_new = node + [num]
                if frozenset(node_new) not in visited:
                    visited.add(frozenset(node_new))
                    queue.append(node_new)
        res = [list(node) for node in visited]
        return res
        

