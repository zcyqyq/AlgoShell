# Last updated: 2025/10/6 16:24:27
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # first use a deque() to simulate stack
        # process tokens
        nums = deque()
        for token in tokens:
            if token == "+":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num1 + num2)
            elif token == "-":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num2 - num1)
            elif token == "*":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num1 * num2)
            elif token == "/":
                num1 = nums.pop()
                num2 = nums.pop()
                res = abs(num2) // abs(num1)
                if (num2 < 0) ^ (num1 < 0):
                    res = -res
                nums.append(res)
            else:
                num = int(token)
                nums.append(num)
        return nums.pop()


        