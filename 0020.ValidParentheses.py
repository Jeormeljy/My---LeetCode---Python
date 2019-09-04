'''

20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"

Output: true

Example 2:

Input: "()[]{}"

Output: true

Example 3:

Input: "(]"

Output: false

Example 4:

Input: "([)]"

Output: false

Example 5:

Input: "{[]}"

Output: true

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        stack = []
        index = 0
        while index < len(s):
            if s[index] == '(':
                stack.append(')')
            elif s[index] == '[':
                stack.append(']')
            elif s[index] == '{':
                stack.append('}')
            elif len(stack) == 0 or stack[-1] != s[index]:
                return False
            else:
                stack.pop()
            index += 1
        return len(stack) == 0
