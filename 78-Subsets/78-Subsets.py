# Last updated: 2025/10/16 17:37:28
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # one method is using frozenset
        # it can store list without order
        # visited = set()
        # res = []
        # queue = deque()
        # queue.append([])
        # visited.add(frozenset([]))
        # while queue:
        #     node = queue.popleft()
        #     for num in nums:
        #         if num in node:
        #             continue
        #         node_new = node + [num]
        #         if frozenset(node_new) not in visited:
        #             visited.add(frozenset(node_new))
        #             queue.append(node_new)
        # res = [list(node) for node in visited]
        # return res

        # kind of weired
        # another method is giving an index

        res = []
        queue = deque()
        queue.append(([], 0))
        while queue:
            node, index = queue.popleft()
            res.append(node)
            for i in range(index, len(nums)):
                num = nums[i]
                if num in node:
                    continue
                node_new = node + [num]
                queue.append((node_new, i + 1))
        return res
        

