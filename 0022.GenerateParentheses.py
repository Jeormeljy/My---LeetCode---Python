'''

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        result = []
        cur = []
        self.DFS(result, cur, n, n)
        return result
    
    def DFS(self, result, cur, left, right):
        if left == 0 and right == 0:
            result.append(''.join(cur))
            return
        if left > 0:
            cur.append('(')
            self.DFS(result, cur, left - 1, right)
            cur.pop()
        if right > left:
            cur.append(')')
            self.DFS(result, cur, left, right - 1)
            cur.pop()
